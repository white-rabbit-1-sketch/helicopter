from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class Water(AbstractMapObject):
    def canCollide(self) -> bool:
        return True