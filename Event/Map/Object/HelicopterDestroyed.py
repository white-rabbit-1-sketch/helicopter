from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class HelicopterDestroyed:
    NAME = "helicopter.destroyed"

    def __init__(self, helicopter: AbstractMapObject) -> None:
        self.helicopter = helicopter