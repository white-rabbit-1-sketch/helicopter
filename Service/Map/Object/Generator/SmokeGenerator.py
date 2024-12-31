import time

from helicopter.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from helicopter.Entity.MapObject.Smoke import Smoke

class SmokeGenerator(AbstractGenerator):
    def createNewSmokeObject(self) -> Smoke:
        return Smoke(self.getRandomObjectImage(), time.time())