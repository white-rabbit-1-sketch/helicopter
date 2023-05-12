import math
import random
from typing import Union, List, Type, Generator

from game.Entity.MapObject.AbstractMapObject import AbstractMapObject
from game.Entity.Map import Map
from game.Entity.MapLayer import MapLayer
from game.Entity.MapLayerCell import MapLayerCell

class MapLayerService:
    def createLayer(self, map: Map, layerName: str) -> MapLayer:
        layer = MapLayer(map)
        map.addLayer(layerName, layer)

        for cell in layer.getCellList():
            cell.nearestCellList = self.getLayerNearestCellListByCell(layer, cell)
            cell.nearestExtendedCellList = self.getLayerNearestExtendedCellListByCell(layer, cell)
            cell.layer = layer

        return layer

    def initNearestCells(self, map) -> None:
        for layerName, layer in map.layers.items():
            for cell in layer.getCellList():
                cell.nearestCellList = self.getLayerNearestCellListByCell(layer, cell)
                cell.nearestExtendedCellList = self.getLayerNearestExtendedCellListByCell(layer, cell)
                cell.layer = layer

    def getLayerNearestExtendedCellListByCell(self, layer: MapLayer, cell: MapLayerCell) -> List[MapLayerCell]:
        result = self.getLayerNearestCellListByCell(layer, cell)

        # Top left
        if cell.y > 0 and cell.x > 0:
            result.append(layer.getCellByPosition(cell.x - 1, cell.y - 1))

        # Top right
        if cell.y > 0 and cell.x < layer.map.colsCount - 1:
            result.append(layer.getCellByPosition(cell.x + 1, cell.y - 1))

        # Down left
        if cell.y < layer.map.rowsCount - 1 and cell.x > 0:
            result.append(layer.getCellByPosition(cell.x - 1, cell.y + 1))

        # Down right
        if cell.y < layer.map.rowsCount - 1 and cell.x < layer.map.colsCount - 1:
            result.append(layer.getCellByPosition(cell.x + 1, cell.y + 1))

        return result


    def getLayerNearestCellListByCell(self, layer: MapLayer, cell: MapLayerCell) -> List[MapLayerCell]:
        result = []

        # Up
        if cell.y > 0:
            result.append(layer.getCellByPosition(cell.x, cell.y - 1))

        # Down
        if cell.y < layer.map.rowsCount - 1:
            result.append(layer.getCellByPosition(cell.x, cell.y + 1))

        # Left
        if cell.x > 0:
            result.append(layer.getCellByPosition(cell.x - 1, cell.y))

        # Right
        if cell.x < layer.map.colsCount - 1:
            result.append(layer.getCellByPosition(cell.x + 1, cell.y))

        return result

    def filterCellListByObject(self, cellList: List[MapLayerCell], object: Type[AbstractMapObject] = None) -> List[MapLayerCell]:
        result = []

        for cell in cellList:
            if object is None and not cell.object is None: continue
            if not object is None and not isinstance(cell.object, object): continue

            result.append(cell)

        return result

    def getLayerCellsCountByPercent(self, layer: MapLayer, percent: int) -> int:
        return math.floor((layer.map.rowsCount * layer.map.colsCount) / 100 * percent)

    def getLayerRandomFreeCell(self, layer: MapLayer) -> Union[MapLayerCell, None]:
        freeCellList = self.filterCellListByObject(layer.getCellList())

        return self.getRandomCellByList(freeCellList)

    def getLayerFreeChainCellList(self, layer: MapLayer, maxCount: int) -> Generator[MapLayerCell, None, None]:
        cellsCount = 0

        cell = None
        while True:
            if not cell: cell = self.getLayerRandomFreeCell(layer) # initial position
            if not cell: break

            yield cell
            cellsCount += 1

            if cellsCount >= maxCount: break

            freeNearestCellList = self.filterCellListByObject(cell.nearestCellList)
            cell = None
            if freeNearestCellList:
                cell = self.getRandomCellByList(freeNearestCellList)

    def getRandomCellByList(self, cellList: List[MapLayerCell], pop: bool = False) -> Union[MapLayerCell, None]:
        result = None

        if cellList:
            index = random.randint(0, len(cellList) - 1)
            result = cellList[index] if not pop else cellList.pop(index)

        return result