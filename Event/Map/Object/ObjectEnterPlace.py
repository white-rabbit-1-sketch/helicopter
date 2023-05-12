from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class ObjectEnterPlace:
    NAME = "object.enter.place"

    def __init__(self, object: AbstractMapObject) -> None:
        self.object = object