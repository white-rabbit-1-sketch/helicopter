from game.Service.Map.Object.Generator.AbstractGenerator import AbstractGenerator
from game.Entity.MapLayer import MapLayer
from game.Entity.MapObject.Grass import Grass

class GrassGenerator(AbstractGenerator):
    def generateGrassOnLayer(self, layer: MapLayer) -> None:
        for cell in layer.getCellList():
            self.mapLayerCellService.setCellObject(cell, self.createNewGrassObject())

    def createNewGrassObject(self) -> Grass:
        return Grass(self.getRandomObjectImage())