from helicopter.Entity.MapObject.AbstractMapObject import AbstractMapObject

class Shop(AbstractMapObject):
    def canCollide(self) -> bool:
        return True