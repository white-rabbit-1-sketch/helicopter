from abc import ABC
from typing import List
import random

from game.Service.Map.MapLayerService import MapLayerService
from game.Service.Map.MapLayerCellService import MapLayerCellService
from game.Entity.Image import Image

class AbstractGenerator(ABC):
    def __init__(self,
        mapLayerService: MapLayerService,
        mapLayerCellService: MapLayerCellService,
        objectImageList: List[Image]
    ) -> None:
        self.mapLayerService = mapLayerService
        self.mapLayerCellService = mapLayerCellService
        self.objectImageList = objectImageList

    def getRandomObjectImage(self) -> Image:
        return self.getRandomObjectImageByList(self.objectImageList)

    def getRandomObjectImageByList(self, imageList: List[Image]) -> Image:
        return imageList[random.randint(0, len(imageList) - 1)]

