from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class Hospital(AbstractMapObject):
    def canCollide(self) -> bool:
        return True