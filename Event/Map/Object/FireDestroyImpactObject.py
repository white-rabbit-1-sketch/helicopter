from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class FireDestroyImpactObject:
    NAME = "fire.destroy.impact.object"

    def __init__(self, object: AbstractMapObject) -> None:
        self.object = object