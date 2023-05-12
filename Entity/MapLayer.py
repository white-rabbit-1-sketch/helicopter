from __future__ import annotations
from typing import List, Union, TYPE_CHECKING

from game.Entity.MapLayerCell import MapLayerCell
if TYPE_CHECKING:
    from game.Entity.Map import Map

class MapLayer:
    def __init__(
        self,
        map: Map
    ) -> None:
        self.map = map
        self.cellList = [[MapLayerCell(x, y, self) for x in range(map.colsCount)] for y in range(map.rowsCount)]

    def getCellByPosition(self, x: int, y: int) -> Union[MapLayerCell, None]:
        return self.cellList[y][x] if y < len(self.cellList) and x < len(self.cellList[y]) else None

    def getCellList(self) -> List[MapLayerCell]:
        result = []

        for x, y in self.map.getCordsGenerator():
            result.append(self.getCellByPosition(x, y))

        return result