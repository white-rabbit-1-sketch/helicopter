import time

from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapObject.Smoke import Smoke

class SmokeGenerator(AbstractGenerator):
    def createNewSmokeObject(self) -> Smoke:
        return Smoke(self.getRandomObjectImage(), time.time())