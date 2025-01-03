from helicopter.Entity.Image import Image

from helicopter.Entity.MapObject.AbstractMapObject import AbstractMapObject

class Smoke(AbstractMapObject):
    def __init__(self, image: Image, createTime: float) -> None:
        AbstractMapObject.__init__(self, image)

        self.createTime = createTime

    def canCollide(self) -> bool:
        return True