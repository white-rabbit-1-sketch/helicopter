from game.Entity.Map import Map
from game.Entity.MapObject import Helicopter
from game.Service.Map.MapLayerService import MapLayerService
from game.Service.Map.Object.Generator.CloudGenerator import CloudGenerator
from game.Service.Map.Object.Generator.EarthGenerator import EarthGenerator
from game.Service.Map.Object.Generator.FireGenerator import FireGenerator
from game.Service.Map.Object.Generator.GrassGenerator import GrassGenerator
from game.Service.Map.Object.Generator.HelicopterGenerator import HelicopterGenerator
from game.Service.Map.Object.Generator.HospitalGenerator import HospitalGenerator
from game.Service.Map.Object.Generator.RockGenerator import RockGenerator
from game.Service.Map.Object.Generator.ShopGenerator import ShopGenerator
from game.Service.Map.Object.Generator.TreeGenerator import TreeGenerator
from game.Service.Map.Object.Generator.WaterGenerator import WaterGenerator
from game.Service.Map.Object.Behavior.CloudBehavior import CloudBehavior
from game.Service.Map.Object.Behavior.FireBehavior import FireBehavior
from game.Service.Map.Object.Behavior.SmokeBehavior import SmokeBehavior
from game.Service.Map.Object.Behavior.HelicopterBehavior import HelicopterBehavior
from game.Entity.MapObject.Tree import Tree
from game.Entity.MapObject.Fire import Fire
from game.Entity.MapObject.Smoke import Smoke

class MainMapGenerator:
    LAYER_GRASS = "grass"
    LAYER_OBJECTS = "objects"
    LAYER_FIRES = "fires"
    LAYER_BASE = "base"
    LAYER_CLOUDS = "clouds"
    LAYER_HELICOPTER = "helicopter"

    def __init__(
        self,
        mapLayerService: MapLayerService,
        cloudGenerator: CloudGenerator,
        earthGenerator: EarthGenerator,
        fireGenerator: FireGenerator,
        grassGenerator: GrassGenerator,
        helicopterGenerator: HelicopterGenerator,
        hospitalGenerator: HospitalGenerator,
        rockGenerator: RockGenerator,
        shopGenerator: ShopGenerator,
        treeGenerator: TreeGenerator,
        waterGenerator: WaterGenerator,
        cloudBehavior: CloudBehavior,
        fireBehavior: FireBehavior,
        smokeBehavior: SmokeBehavior,
        helicopterBehavior: HelicopterBehavior,
        mapRowsCount: int,
        mapColsCount: int,
        waterPercent: int,
        rockPercent: int,
        totalTreePercent: int,
        singleTreePercent: int,
        treeFirePercent: int,
        earthPercent: int,
        normalCloudPercent: int,
        lightningCloudPercent: int,
        rainingCloudPercent: int,
        rainbowCloudPercent: int
    ):
        self.mapLayerService = mapLayerService
        self.cloudGenerator = cloudGenerator
        self.earthGenerator = earthGenerator
        self.fireGenerator = fireGenerator
        self.grassGenerator = grassGenerator
        self.helicopterGenerator = helicopterGenerator
        self.hospitalGenerator = hospitalGenerator
        self.rockGenerator = rockGenerator
        self.shopGenerator = shopGenerator
        self.treeGenerator = treeGenerator
        self.waterGenerator = waterGenerator
        self.cloudBehavior = cloudBehavior
        self.fireBehavior = fireBehavior
        self.smokeBehavior = smokeBehavior
        self.helicopterBehavior = helicopterBehavior
        self.mapRowsCount = mapRowsCount
        self.mapColsCount = mapColsCount
        self.waterPercent = waterPercent
        self.rockPercent = rockPercent
        self.totalTreePercent = totalTreePercent
        self.singleTreePercent = singleTreePercent
        self.treeFirePercent = treeFirePercent
        self.earthPercent = earthPercent
        self.normalCloudPercent = normalCloudPercent
        self.lightningCloudPercent = lightningCloudPercent
        self.rainingCloudPercent = rainingCloudPercent
        self.rainbowCloudPercent = rainbowCloudPercent

    def generateMap(self) -> Map:
        map = Map(self.mapRowsCount, self.mapColsCount)

        grassLayer = self.mapLayerService.createLayer(map, self.LAYER_GRASS)
        objectsLayer = self.mapLayerService.createLayer(map, self.LAYER_OBJECTS)
        firesLayer = self.mapLayerService.createLayer(map, self.LAYER_FIRES)
        cloudsLayer = self.mapLayerService.createLayer(map, self.LAYER_CLOUDS)

        self.grassGenerator.generateGrassOnLayer(grassLayer)
        self.waterGenerator.generateWaterOnLayer(objectsLayer, self.waterPercent)
        self.rockGenerator.generateRocksOnLayer(objectsLayer, self.rockPercent)
        self.treeGenerator.generateTreesOnLayer(objectsLayer, self.totalTreePercent, self.singleTreePercent)
        self.fireGenerator.generateTreesFiresOnLayer(firesLayer, objectsLayer, self.treeFirePercent)
        self.earthGenerator.generateEarthOnLayer(objectsLayer, self.earthPercent)
        self.shopGenerator.generateShopOnLayer(objectsLayer)
        self.hospitalGenerator.generateHospitalOnLayer(objectsLayer)
        self.cloudGenerator.generateNormalCloudsOnLayer(cloudsLayer, self.normalCloudPercent)
        self.cloudGenerator.generateLightningCloudsOnLayer(cloudsLayer, self.lightningCloudPercent)
        self.cloudGenerator.generateRainingCloudsOnLayer(cloudsLayer, self.rainingCloudPercent)
        self.cloudGenerator.generateRainbowCloudsOnLayer(cloudsLayer, self.rainbowCloudPercent)

        return map

    def createHelicopterOnMap(self, map: Map) -> Helicopter:
        helicopterLayer = self.mapLayerService.createLayer(map, self.LAYER_HELICOPTER)
        objectsLayer = map.getLayerByName(self.LAYER_OBJECTS)

        return self.helicopterGenerator.generateHelicopterOnLayer(helicopterLayer, objectsLayer)

    def handleBehavior(self, map: Map) -> None:
        objectsLayer = map.getLayerByName(self.LAYER_OBJECTS)
        firesLayer = map.getLayerByName(self.LAYER_FIRES)
        cloudsLayer = map.getLayerByName(self.LAYER_CLOUDS)

        for fireCell in firesLayer.getCellList():
            if not fireCell.object: continue

            if isinstance(fireCell.object, Fire):
                self.fireBehavior.handleFire(fireCell.object, objectsLayer, [Tree])
            elif isinstance(fireCell.object, Smoke):
                self.smokeBehavior.handleSmoke(fireCell.object)

        for cloudCell in cloudsLayer.getCellList():
            if not cloudCell.object: continue

            self.cloudBehavior.handleCloud(cloudCell.object)

        self.treeGenerator.generateTreesOnLayer(objectsLayer, self.totalTreePercent, self.singleTreePercent)
        self.fireGenerator.generateTreesFiresOnLayer(firesLayer, objectsLayer, self.treeFirePercent)