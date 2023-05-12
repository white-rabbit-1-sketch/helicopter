from pydispatch import dispatcher
import time

from game.Service.Map.Object.Behavior.AbstractObjectBehavior import AbstractObjectBehavior
from game.Entity.MapObject.Helicopter import Helicopter
from game.Service.Map.MapLayerCellService import MapLayerCellService
from game.Event.Map.Object.ObjectEnterPlace import ObjectEnterPlace
from game.Event.Map.Object.HelicopterDestroyed import HelicopterDestroyed
from game.Entity.MapObject.Cloud.LightningCloud import LightningCloud
from game.Entity.MapObject.Fire import Fire
from game.Entity.MapObject.Water import Water
from game.Entity.MapObject.Shop import Shop
from game.Entity.MapObject.Hospital import Hospital
from game.Service.Map.Object.Behavior.FireBehavior import FireBehavior

class HelicopterBehavior(AbstractObjectBehavior):
    def __init__(self,
        mapLayerCellService: MapLayerCellService,
        fireBehavior: FireBehavior
    ) -> None:
        AbstractObjectBehavior.__init__(self, mapLayerCellService)

        self.fireBehavior = fireBehavior

        dispatcher.connect(self.onObjectEnterPlace, signal=ObjectEnterPlace.NAME)

    def moveHelicopterUp(self, helicopter: Helicopter) -> None:
        self.moveHelicopter(helicopter, helicopter.cell.x, helicopter.cell.y - 1)

    def moveHelicopterDown(self, helicopter: Helicopter) -> None:
        self.moveHelicopter(helicopter, helicopter.cell.x, helicopter.cell.y + 1)

    def moveHelicopterLeft(self, helicopter: Helicopter) -> None:
        self.moveHelicopter(helicopter, helicopter.cell.x - 1, helicopter.cell.y)

    def moveHelicopterRight(self, helicopter: Helicopter) -> None:
        self.moveHelicopter(helicopter, helicopter.cell.x + 1, helicopter.cell.y)

    def canHelicopterMove(self, helicopter: Helicopter) -> bool:
        result = False

        currentTime = time.time()

        if not helicopter.lastMoveTime or currentTime - helicopter.lastMoveTime >= 1 / helicopter.speed:
            result = True
            helicopter.lastMoveTime = currentTime

        return result

    def moveHelicopter(self, helicopter: Helicopter, targetX: int, targetY: int) -> None:
        if targetX >= 0 and targetY >= 0:
            targetCell = helicopter.cell.layer.getCellByPosition(targetX, targetY)
            if targetCell:
                self.mapLayerCellService.setCellObject(targetCell, helicopter)

    def onObjectEnterPlace(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: ObjectEnterPlace = data.get('event')

        helicopter: Helicopter = event.object.cell.layer.map.scene.player.helicopter
        helicopterCell = helicopter.cell

        # Cloud has met a helicopter
        if isinstance(event.object, LightningCloud) and event.object.cell.x == helicopterCell.x and event.object.cell.y == helicopterCell.y:
            self.applyHelicopterDamage(helicopter)

        # Helicopter has met ...
        if isinstance(event.object, Helicopter):
            for layerName, layer in helicopterCell.layer.map.layers.items():
                placeCell = layer.getCellByPosition(helicopterCell.x, helicopterCell.y)

                if not placeCell.object: continue

                # Helicopter has met a lightning cloud
                if isinstance(placeCell.object, LightningCloud):
                    self.applyHelicopterDamage(helicopter)

    def applyHelicopterDamage(self, helicopter: Helicopter) -> None:
        helicopter.currentHealth -= 1

        if helicopter.currentHealth <= 0:
            dispatcher.send(signal=HelicopterDestroyed.NAME, sender=None, data={"event": HelicopterDestroyed(helicopter)})

    def canHelicopterGrabWater(self, helicopter: Helicopter) -> bool:
        object = self.mapLayerCellService.getCellCollisionByObjectType(helicopter.cell, Water)

        return True if object and helicopter.waterVolume < helicopter.waterCapacity else False

    def canHelicopterExtinguishFire(self, helicopter: Helicopter) -> bool:
        object = self.mapLayerCellService.getCellCollisionByObjectType(helicopter.cell, Fire)

        return True if object and helicopter.waterVolume > 0 else False

    def canHelicopterHeal(self, helicopter: Helicopter) -> bool:
        object = self.mapLayerCellService.getCellCollisionByObjectType(helicopter.cell, Hospital)

        return True if object and helicopter.currentHealth < helicopter.maxHealth else False

    def canHelicopterUpgrade(self, helicopter: Helicopter) -> bool:
        object = self.mapLayerCellService.getCellCollisionByObjectType(helicopter.cell, Shop)

        return True if object else False

    def upgradeHelicopter(self, helicopter: Helicopter) -> None:
        helicopter.waterCapacity += 1

    def healHelicopter(self, helicopter: Helicopter) -> None:
        helicopter.currentHealth += 1

    def grabWaterByHelicopter(self, helicopter: Helicopter) -> None:
        helicopter.waterVolume += 1

    def extinguishFireByHelicopter(self, helicopter: Helicopter) -> None:
        fire: Fire = self.mapLayerCellService.getCellCollisionByObjectType(helicopter.cell, Fire)
        self.fireBehavior.extinguishFire(fire)
        helicopter.waterVolume -= 1