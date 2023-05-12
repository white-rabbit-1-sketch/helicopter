from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Entity.MapObject.Water import Water

class WaterGenerator(AbstractGenerator):
    def generateWaterOnLayer(self, layer: MapLayer, percent: int) -> None:
        freeChainCellList = self.mapLayerService.getLayerFreeChainCellList(
            layer,
            self.mapLayerService.getLayerCellsCountByPercent(layer, percent)
        )

        for cell in freeChainCellList:
            self.mapLayerCellService.setCellObject(cell, self.createNewWaterObject())

    def createNewWaterObject(self) -> Water:
        return Water(self.getRandomObjectImage())