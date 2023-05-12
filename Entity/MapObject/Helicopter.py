from game.Entity.MapObject.AbstractPlayerMapObject import AbstractPlayerMapObject
from game.Entity.Image import Image

class Helicopter(AbstractPlayerMapObject):
    def __init__(
            self,
            image: Image,
            waterCapacity: int,
            maxHealth: int,
            speed: float,
    ):
        AbstractPlayerMapObject.__init__(self, image)

        self.waterCapacity = waterCapacity
        self.waterVolume = waterCapacity

        self.maxHealth = maxHealth
        self.currentHealth = maxHealth

        self.speed = speed

        self.lastMoveTime = None

    def canCollide(self) -> bool:
        return True

    def getMaxHealth(self) -> int:
        return self.maxHealth

    def getCurrentHealth(self) -> int:
        return self.currentHealth

    def getWaterCapacity(self) -> int:
        return self.waterCapacity

    def getWaterVolume(self) -> int:
        return  self.waterVolume