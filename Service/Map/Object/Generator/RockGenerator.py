from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Entity.MapObject.Rock import Rock

class RockGenerator(AbstractGenerator):
    def generateRocksOnLayer(self, layer: MapLayer, percent: int) -> None:
        freeChainCellList = self.mapLayerService.getLayerFreeChainCellList(
            layer,
            self.mapLayerService.getLayerCellsCountByPercent(layer, percent)
        )

        for cell in freeChainCellList:
            self.mapLayerCellService.setCellObject(cell, self.createNewRockObject())

    def createNewRockObject(self) -> Rock:
        return Rock(self.getRandomObjectImage())

