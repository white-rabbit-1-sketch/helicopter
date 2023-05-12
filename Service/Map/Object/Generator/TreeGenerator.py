import math

from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Entity.MapObject.Tree import Tree

class TreeGenerator(AbstractGenerator):
    def generateTreesOnLayer(self, layer: MapLayer, rotalTreePercent: int, singleTreePercent: int) -> None:
        currentTreeCount = len(self.mapLayerService.filterCellListByObject(
            layer.getCellList(),
            Tree
        ))
        maxTreeCount = self.mapLayerService.getLayerCellsCountByPercent(layer, rotalTreePercent)
        randomTreeCount = math.floor(maxTreeCount / 100 * singleTreePercent)

        # Create tree chains
        freeChainCellList = self.mapLayerService.getLayerFreeChainCellList(
            layer,
            self.mapLayerService.getLayerCellsCountByPercent(layer, rotalTreePercent)
        )
        for cell in freeChainCellList:
            if currentTreeCount >= maxTreeCount - randomTreeCount: break
            self.mapLayerCellService.setCellObject(cell, self.createNewTreeObject())
            currentTreeCount += 1

        # Create random trees
        while currentTreeCount < maxTreeCount:
            cell = self.mapLayerService.getLayerRandomFreeCell(layer)

            if not cell: break

            self.mapLayerCellService.setCellObject(cell, self.createNewTreeObject())
            currentTreeCount += 1

    def createNewTreeObject(self) -> Tree:
        return Tree(self.getRandomObjectImage())



