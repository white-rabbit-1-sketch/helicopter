from __future__ import annotations
from typing import TYPE_CHECKING, Union
from abc import ABC

if TYPE_CHECKING:
    from game.Entity.MapLayerCell import MapLayerCell

from game.Entity.Image import Image

class AbstractMapObject(ABC):
    def __init__(self, image: Image) -> None:
        self.cell: Union[MapLayerCell, None] = None
        self.image: Image = image

    def getImage(self) -> Image:
        return self.image

    def canCollide(self) -> bool:
        return False