from game.Entity.MapObject.Shop import Shop
from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Entity.MapObject.Hospital import Hospital

class HospitalGenerator(AbstractGenerator):
    def generateHospitalOnLayer(self, layer: MapLayer) -> None:
        shopCell = self.mapLayerService.getRandomCellByList(self.mapLayerService.filterCellListByObject(
            layer.getCellList(),
            Shop
        ))

        shopNearestCell = self.mapLayerService.getRandomCellByList(shopCell.nearestCellList)
        self.mapLayerCellService.setCellObject(shopNearestCell, self.createNewHospitalObject())

    def createNewHospitalObject(self) -> Hospital:
        return Hospital(self.getRandomObjectImage())

