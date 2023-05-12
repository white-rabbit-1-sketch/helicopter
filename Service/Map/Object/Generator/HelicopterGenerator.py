from typing import List

from game.Entity.Image import Image
from game.Entity.MapObject.Shop import Shop
from game.Entity.MapObject.Helicopter import Helicopter
from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Service.Map.MapLayerService import MapLayerService
from game.Service.Map.MapLayerCellService import MapLayerCellService

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



