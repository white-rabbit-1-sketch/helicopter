from __future__ import annotations
from typing import Union, Generator, Tuple, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from game.Entity.Scene import Scene

from game.Entity.MapLayer import MapLayer

class Map:
    def __init__(
        self,
        rowsCount: int,
        colsCount: int
    ) -> None:
        self.rowsCount = rowsCount
        self.colsCount = colsCount
        self.layers: Dict[str, MapLayer] = {}
        self.scene: Union[Scene, None] = None

    def getCordsGenerator(self) -> Generator[Tuple[int, int], None, None]:
        for y in range(self.rowsCount):
            for x in range(self.colsCount):
                yield x, y

    def addLayer(self, name: str, layer: MapLayer) -> None:
        self.layers[name] = layer

    def getLayerByName(self, name: str) -> MapLayer:
        return self.layers[name]