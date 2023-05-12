import time

from game.Service.Map.Object.Behavior.AbstractObjectBehavior import AbstractObjectBehavior
from game.Entity.MapObject.Smoke import Smoke
from game.Service.Map.MapLayerCellService import MapLayerCellService

class SmokeBehavior(AbstractObjectBehavior):
    def __init__(
        self,
        mapLayerCellService: MapLayerCellService,
        smokeLifeTime: int
    ) -> None:
        AbstractObjectBehavior.__init__(self, mapLayerCellService)

        self.smokeLifeTime = smokeLifeTime

    def handleSmoke(self, smoke: Smoke) -> None:
        currentTime = time.time()

        if currentTime - smoke.createTime >= self.smokeLifeTime:
            self.mapLayerCellService.setCellObject(smoke.cell, None)