from typing import Callable, Type, List

from helicopter.Service.Map.MapLayerService import MapLayerService
from helicopter.Service.Map.MapLayerCellService import MapLayerCellService
from helicopter.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from helicopter.Entity.MapLayer import MapLayer
from helicopter.Entity.MapObject.Cloud.AbstractCloud import AbstractCloud
from helicopter.Entity.MapObject.AbstractMapObject import AbstractMapObject
from helicopter.Entity.MapObject.Cloud.NormalCloud import NormalCloud
from helicopter.Entity.MapObject.Cloud.LightningCloud import LightningCloud
from helicopter.Entity.MapObject.Cloud.RainingCloud import RainingCloud
from helicopter.Entity.MapObject.Cloud.RainbowCloud import RainbowCloud
from helicopter.Entity.Image import Image

class CloudGenerator(AbstractGenerator):
    def __init__(
            self,
            mapLayerService: MapLayerService,
            mapLayerCellService: MapLayerCellService,
            normalCloudImageList: List[Image],
            lightningCloudImageList: List[Image],
            rainingCloudImageList: List[Image],
            rainbowCloudImageList: List[Image]
    ):
        AbstractGenerator.__init__(self, mapLayerService, mapLayerCellService, [])

        self.normalCloudImageList = normalCloudImageList
        self.lightningCloudImageList = lightningCloudImageList
        self.rainingCloudImageList = rainingCloudImageList
        self.rainbowCloudImageList = rainbowCloudImageList

    def generateNormalCloudsOnLayer(self, layer: MapLayer, percent: int) -> None:
        self.generateCloudsByCloudType(layer, lambda: self.createNewNormalCloudObject(), percent)

    def generateLightningCloudsOnLayer(self, layer: MapLayer, percent: int) -> None:
        self.generateCloudsByCloudType(layer, lambda: self.createNewLightningCloudObject(), percent)

    def generateRainingCloudsOnLayer(self, layer: MapLayer, percent: int) -> None:
        self.generateCloudsByCloudType(layer, lambda: self.createNewRainingCloudObject(), percent)

    def generateRainbowCloudsOnLayer(self, layer: MapLayer, percent: int) -> None:
        self.generateCloudsByCloudType(layer, lambda: self.createNewRainbowCloudObject(), percent)

    def generateCloudsByCloudType(
            self,
            layer: MapLayer,
            cloudCreator: Callable[[], AbstractCloud],
            percent: int,
    ) -> None:
        maxCloudCount = self.mapLayerService.getLayerCellsCountByPercent(layer, percent)
        currentCloudCount = 0

        while currentCloudCount < maxCloudCount:
            cell = self.mapLayerService.getLayerRandomFreeCell(layer)
            if not cell: break

            self.mapLayerCellService.setCellObject(
                cell,
                cloudCreator()
            )

            currentCloudCount += 1

    def createNewCloudObjectByCloudType(
            self,
            cloudType: Type[AbstractMapObject],
            cloudImageList: List[Image]
    ) -> AbstractCloud:
        return cloudType(self.getRandomObjectImageByList(cloudImageList))

    def createNewNormalCloudObject(self) -> NormalCloud:
        return self.createNewCloudObjectByCloudType(NormalCloud, self.normalCloudImageList)

    def createNewLightningCloudObject(self) -> LightningCloud:
        return self.createNewCloudObjectByCloudType(LightningCloud, self.lightningCloudImageList)

    def createNewRainingCloudObject(self) -> RainingCloud:
        return self.createNewCloudObjectByCloudType(RainingCloud, self.rainingCloudImageList)

    def createNewRainbowCloudObject(self) -> RainbowCloud:
        return self.createNewCloudObjectByCloudType(RainbowCloud, self.rainbowCloudImageList)