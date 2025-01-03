from abc import ABC

from helicopter.Entity.Image import Image
from helicopter.Entity.MapObject.AbstractMapObject import AbstractMapObject

class AbstractCloud(AbstractMapObject, ABC):
    def __init__(self, image: Image) -> None:
        AbstractMapObject.__init__(self, image)

        self.lastMovementTime = None


    def canCollide(self) -> bool:
        return True