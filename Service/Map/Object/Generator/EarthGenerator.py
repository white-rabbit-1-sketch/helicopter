from helicopter.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from helicopter.Entity.MapLayer import MapLayer
from helicopter.Entity.MapObject.Earth import Earth

class EarthGenerator(AbstractGenerator):
    def generateEarthOnLayer(self, layer: MapLayer, percent: int) -> None:
        maxEarthCount = self.mapLayerService.getLayerCellsCountByPercent(layer, percent)
        currentEarthCount = 0

        while currentEarthCount < maxEarthCount:
            cell = self.mapLayerService.getLayerRandomFreeCell(layer)
            if not cell: break

            self.mapLayerCellService.setCellObject(cell, self.createNewEarthObject())
            currentEarthCount += 1

    def createNewEarthObject(self) -> Earth:
        return Earth(self.getRandomObjectImage())