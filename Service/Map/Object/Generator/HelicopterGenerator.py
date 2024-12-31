from typing import List

from helicopter.Entity.Image import Image
from helicopter.Entity.MapObject.Shop import Shop
from helicopter.Entity.MapObject.Helicopter import Helicopter
from helicopter.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from helicopter.Entity.MapLayer import MapLayer
from helicopter.Service.Map.MapLayerService import MapLayerService
from helicopter.Service.Map.MapLayerCellService import MapLayerCellService

class HelicopterGenerator(AbstractGenerator):
    def __init__(
        self,
        mapLayerService: MapLayerService,
        mapLayerCellService: MapLayerCellService,
        objectImageList: List[Image],
        helicopterWaterCapacity: int,
        helicopterMaxHealth: int,
        helicopterSpeed: float,
    ):
        AbstractGenerator.__init__(self, mapLayerService, mapLayerCellService, objectImageList)

        self.helicopterWaterCapacity = helicopterWaterCapacity
        self.helicopterMaxHealth = helicopterMaxHealth
        self.helicopterSpeed = helicopterSpeed

    def generateHelicopterOnLayer(
            self,
            helicopterLayer: MapLayer,
            shopLayer: MapLayer
    ) -> Helicopter:
        shopCell = self.mapLayerService.getRandomCellByList(self.mapLayerService.filterCellListByObject(
            shopLayer.getCellList(),
            Shop
        ))

        helicopterCell = helicopterLayer.getCellByPosition(shopCell.x, shopCell.y)
        helicopter = self.createNewHelicopterObject()
        self.mapLayerCellService.setCellObject(helicopterCell, helicopter)

        return helicopter

    def createNewHelicopterObject(self) -> Helicopter:
        return Helicopter(
            self.getRandomObjectImage(),
            self.helicopterWaterCapacity,
            self.helicopterMaxHealth,
            self.helicopterSpeed
        )



