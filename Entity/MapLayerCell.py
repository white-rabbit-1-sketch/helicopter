from __future__ import annotations
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from game.Entity.MapLayer import MapLayer

from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class MapLayerCell:
    def __init__(
        self,
        x: int,
        y: int,
        layer: MapLayer
    ) -> None:
        self.x = x
        self.y = y
        self.object: Union[AbstractMapObject, None] = None
        self.layer = layer
        self.nearestCellList = []
        self.nearestExtendedCellList = []

    def __getstate__(self):
        return {
            'x': self.x,
            'y': self.y,
            'object': self.object,
            #'nearestCellList': self.nearestCellList,
            #'nearestExtendedCellList': self.nearestExtendedCellList,
        }