import math
import time

from helicopter.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from helicopter.Entity.MapLayer import MapLayer
from helicopter.Entity.MapObject.Tree import Tree
from helicopter.Entity.MapObject.Fire import Fire

class FireGenerator(AbstractGenerator):
    def generateTreesFiresOnLayer(
            self,
            fireLayer: MapLayer,
            treeLayer: MapLayer,
            treeFirePercent: int
    ) -> None:
        treeCellList = self.mapLayerService.filterCellListByObject(
            treeLayer.getCellList(),
            Tree
        )

        notBurningTreeCellList = []
        for cellTree in treeCellList:
            fireCell = fireLayer.getCellByPosition(cellTree.x, cellTree.y)

            if fireCell.object: continue # There is a fire or a smoke

            notBurningTreeCellList.append(cellTree)

        treeCount = len(treeCellList)
        currentBurningTreeCount = treeCount - len(notBurningTreeCellList)

        maxBurningTreeCount = math.floor(treeCount / 100 * treeFirePercent)
        while currentBurningTreeCount < maxBurningTreeCount and notBurningTreeCellList:
            treeCell = self.mapLayerService.getRandomCellByList(notBurningTreeCellList, True)
            fireCell = fireLayer.getCellByPosition(treeCell.x, treeCell.y)
            self.mapLayerCellService.setCellObject(fireCell, self.createNewFireObject())

            currentBurningTreeCount += 1

    def createNewFireObject(self) -> Fire:
        return Fire(self.getRandomObjectImage(), time.time())