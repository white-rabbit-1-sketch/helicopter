from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Entity.MapObject.Shop import Shop

class ShopGenerator(AbstractGenerator):
    def generateShopOnLayer(self, layer: MapLayer) -> None:
        cell = self.mapLayerService.getLayerRandomFreeCell(layer)
        self.mapLayerCellService.setCellObject(cell, self.createNewShopObject())

    def createNewShopObject(self) -> Shop:
        return Shop(self.getRandomObjectImage())