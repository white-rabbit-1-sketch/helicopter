from helicopter.Entity.MapObject.Shop import Shop
from helicopter.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from helicopter.Entity.MapLayer import MapLayer
from helicopter.Entity.MapObject.Hospital import Hospital

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

