from abc import ABC

from game.Entity.Scene import Scene

class AbstractSceneEvent(ABC):
    def __init__(self, scene: Scene):
        self.scene = scene