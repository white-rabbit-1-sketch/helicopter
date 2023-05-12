from __future__ import annotations
from abc import ABC, abstractmethod

from game.Entity.MapObject.AbstractMapObject import AbstractMapObject

class AbstractPlayerMapObject(AbstractMapObject, ABC):
    @abstractmethod
    def getMaxHealth(self) -> int:
        pass

    @abstractmethod
    def getCurrentHealth(self) -> int:
        pass

    def getWaterCapacity(self) -> int:
        pass

    @abstractmethod
    def getWaterVolume(self) -> int:
        pass