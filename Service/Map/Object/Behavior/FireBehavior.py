import time
from typing import Type, List
from pydispatch import dispatcher

from game.Service.Map.Object.Behavior.AbstractObjectBehavior import AbstractObjectBehavior
from game.Entity.MapObject.Fire import Fire
from game.Entity.MapObject.Cloud.RainingCloud import RainingCloud
from game.Entity.MapLayer import MapLayer
from game.Service.Map.MapLayerCellService import MapLayerCellService
from game.Entity.MapObject.AbstractMapObject import AbstractMapObject
from game.Service.Map.Object.Generator.FireGenerator import FireGenerator
from game.Service.Map.Object.Generator.SmokeGenerator import SmokeGenerator
from game.Event.Map.Object.FireDestroyImpactObject import FireDestroyImpactObject
from game.Event.Map.Object.ObjectEnterPlace import ObjectEnterPlace

class FireBehavior(AbstractObjectBehavior):
    def __init__(self,
        mapLayerCellService: MapLayerCellService,
        fireGenerator: FireGenerator,
        smokeGenerator: SmokeGenerator,
        burningPeriod: int,
        distributionPeriod: int
    ) -> None:
        AbstractObjectBehavior.__init__(self, mapLayerCellService)

        self.fireGenerator = fireGenerator
        self.smokeGenerator = smokeGenerator
        self.burningPeriod = burningPeriod
        self.distributionPeriod = distributionPeriod

        dispatcher.connect(self.onObjectEnterPlace, signal=ObjectEnterPlace.NAME)

    def handleFire(
        self,
        fire: Fire,
        impactLayer: MapLayer,
        impactObjectTypeList: List[Type[AbstractMapObject]]
    ) -> None:
        currentTime = int(time.time())
        fireCreateTime = int(fire.createTime)

        fireCell = fire.cell

        if currentTime - fireCreateTime >= self.burningPeriod:
            dispatcher.send(signal=FireDestroyImpactObject.NAME, sender=None, data={"event": FireDestroyImpactObject(fireCell.object)})

            self.mapLayerCellService.setCellObject(impactLayer.getCellByPosition(fireCell.x, fireCell.y), None)
            self.extinguishFire(fire)
        elif ((currentTime - fireCreateTime) % self.distributionPeriod == 0) and currentTime - fireCreateTime > 0:
            # We need to reset create time in order to valid refire
            for nearestCell in fireCell.nearestCellList:
                targetFireCell = fireCell.layer.getCellByPosition(nearestCell.x, nearestCell.y)
                targetImpactCell = impactLayer.getCellByPosition(nearestCell.x, nearestCell.y)

                if targetFireCell.object: continue  # Already have an object (e.g. fire or smoke)
                if not targetImpactCell.object: continue  # No object on impact cell
                if not any(isinstance(targetImpactCell.object, t) for t in impactObjectTypeList): continue # No valid object on impact cell)
                self.mapLayerCellService.setCellObject(targetFireCell, self.fireGenerator.createNewFireObject())

    def extinguishFire(self, fire: Fire) -> None:
        self.mapLayerCellService.setCellObject(fire.cell, self.smokeGenerator.createNewSmokeObject())

    def onObjectEnterPlace(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: ObjectEnterPlace = data.get('event')

        # Fire has met a RainingCloud
        if isinstance(event.object, RainingCloud):
            fire = self.mapLayerCellService.getCellCollisionByObjectType(event.object.cell, Fire)
            if fire:
                self.mapLayerCellService.setCellObject(fire.cell, None)