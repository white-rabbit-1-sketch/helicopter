from pydispatch import dispatcher

from game.Service.System.ParameterService import ParameterService
from game.Service.Map.Level.MainMapGenerator import MainMapGenerator
from game.Service.Scene.MainSceneGenerator import MainSceneGenerator
from game.Service.Map.MapLayerService import MapLayerService
from game.Service.Hardware.Controller.KeyboardControllerService import KeyboardControllerService
from game.Service.Player.PlayerService import PlayerService
from game.EventSubscriber.PlayerEventSubscriber import PlayerEventSubscriber
from game.Service.Hardware.Renderer.OpenGLRenderer import OpenGLRenderer
from game.Service.System.ImageService import ImageService
from game.Service.Map.MapLayerCellService import MapLayerCellService
from game.Service.Map.Object.Generator.CloudGenerator import CloudGenerator
from game.Service.Map.Object.Generator.EarthGenerator import EarthGenerator
from game.Service.Map.Object.Generator.FireGenerator import FireGenerator
from game.Service.Map.Object.Generator.SmokeGenerator import SmokeGenerator
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
from game.Event.PreLoadService import PreLoadService


class ServiceLoader:
    def __init__(self, parameterService: ParameterService) -> None:
        self.parameterService = parameterService

    def loadRenderer(self) -> None:
        self.imageService = ImageService()

        ### RENDERER ###
        self.openGLRenderer = OpenGLRenderer(
            self.imageService,
            self.parameterService.getScreenWindowCaption(),
            self.parameterService.getScreenWidth(),
            self.parameterService.getScreenHeight(),
            self.parameterService.getScreenFps(),
            self.parameterService.getScreenAnimationSpeed(),
            self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight()
        )

    def loadCommon(self) -> None:
        ### MAP RESOURCES ###
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: grass images")})
        self.grassImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryGrass(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: water images")})
        self.waterImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryWater(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: rock images")})
        self.rocksImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryRocks(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: tree images")})
        self.treeImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryTrees(),
                                                              self.parameterService.getScreenMapObjectWidth(),
                                                              self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: earth images")})
        self.earthImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryEarth(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: shop images")})
        self.shopsImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryShops(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: hospital images")})
        self.hospitalsImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectoryHospitals(), self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: normal cloud images")})
        self.normalCloudsImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectoryCloudsNormal(), self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: lightning cloud images")})
        self.lightningCloudsImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectoryCloudsLightning(),
            self.parameterService.getScreenMapObjectWidth(), self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: raining cloud images")})
        self.rainingCloudsImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectoryCloudsRaining(), self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: rainbow cloud images")})
        self.rainbowCloudsImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectoryCloudsRainbow(), self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: wall images")})
        self.wallsImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryWalls(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: fire images")})
        self.firesImageList = self.imageService.buildImageList(self.parameterService.getMapImageDirectoryFires(),
                                                               self.parameterService.getScreenMapObjectWidth(),
                                                               self.parameterService.getScreenMapObjectHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: helicopter images")})
        self.helicoptersImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectoryHelicopters(), self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight())

        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: smoke images")})
        self.smokeImageList = self.imageService.buildImageList(
            self.parameterService.getMapImageDirectorySmoke(), self.parameterService.getScreenMapObjectWidth(),
            self.parameterService.getScreenMapObjectHeight())

        ### RENDERER RESOURCES ###
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: health icon image")})
        self.healthIconImage = self.imageService.buildImage(self.parameterService.getInterfaceImageHealthIcon(),
                                                            self.parameterService.getInterfaceImageHealthIconWidth(),
                                                            self.parameterService.getInterfaceImageHealthHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: trophy icon image")})
        self.trophyIconImage = self.imageService.buildImage(self.parameterService.getInterfaceImageTrophyIcon(),
                                                            self.parameterService.getInterfaceImageTrophyIconWidth(),
                                                            self.parameterService.getInterfaceImageTrophyHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: water icon image")})
        self.waterIconImage = self.imageService.buildImage(self.parameterService.getInterfaceImageWaterIcon(),
                                                           self.parameterService.getInterfaceImageWaterIconWidth(),
                                                           self.parameterService.getInterfaceImageWaterHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: health icon image")})
        self.fireIconImage = self.imageService.buildImage(self.parameterService.getInterfaceImageFireIcon(),
                                                          self.parameterService.getInterfaceImageFireWidth(),
                                                          self.parameterService.getInterfaceImageFireHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: pale fire image")})
        self.extinguishedFireIconImage = self.imageService.buildImage(
            self.parameterService.getInterfaceImageExtinguishedFireIcon(),
            self.parameterService.getInterfaceImageExtinguishedFireWidth(),
            self.parameterService.getInterfaceImageExtinguishedFireHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: pale health image")})
        self.paleHealthIconImage = self.imageService.buildImage(self.parameterService.getInterfaceImagePaleHealthIcon(),
                                                                self.parameterService.getInterfaceImagePaleHealthWidth(),
                                                                self.parameterService.getInterfaceImagePaleHealthHeight())
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("build resource: pale water image")})
        self.paleWaterIconImage = self.imageService.buildImage(self.parameterService.getInterfaceImagePaleWaterIcon(),
                                                               self.parameterService.getInterfaceImagePaleWaterWidth(),
                                                               self.parameterService.getInterfaceImagePaleWaterHeight())

        ### RENDERER POST INITIALIZATION ###
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("initialize renderer")})
        self.openGLRenderer.healthIconImage = self.healthIconImage
        self.openGLRenderer.trophyIconImage = self.trophyIconImage
        self.openGLRenderer.waterIconImage = self.waterIconImage
        self.openGLRenderer.fireIconImage = self.fireIconImage
        self.openGLRenderer.extinguishedFireIconImage = self.extinguishedFireIconImage
        self.openGLRenderer.paleHealthIconImage = self.paleHealthIconImage
        self.openGLRenderer.paleWaterIconImage = self.paleWaterIconImage

        ### Map ###
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("initialize map services")})
        self.mapLayerService = MapLayerService()
        self.mapLayerCellService = MapLayerCellService()

        ### Generators ###
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("initialize map generators")})
        self.cloudGenerator = CloudGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.normalCloudsImageList,
            self.lightningCloudsImageList,
            self.rainingCloudsImageList,
            self.rainbowCloudsImageList
        )
        self.earthGenerator = EarthGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.earthImageList
        )
        self.smokeGenerator = SmokeGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.smokeImageList
        )
        self.fireGenerator = FireGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.firesImageList
        )
        self.grassGenerator = GrassGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.grassImageList
        )
        self.helicopterGenerator = HelicopterGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.helicoptersImageList,
            self.parameterService.getObjectSettingsHelicopterWaterCapacity(),
            self.parameterService.getObjectSettingsHelicopterMaxHealth(),
            self.parameterService.getObjectSettingsHelicopterMoveSpeed(),
        )
        self.hospitalGenerator = HospitalGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.hospitalsImageList
        )
        self.rockGenerator = RockGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.rocksImageList
        )
        self.shopGenerator = ShopGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.shopsImageList
        )
        self.treeGenerator = TreeGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.treeImageList
        )
        self.waterGenerator = WaterGenerator(
            self.mapLayerService,
            self.mapLayerCellService,
            self.waterImageList
        )

        ### Behaviors ###
        self.cloudBehavior = CloudBehavior(
            self.mapLayerCellService,
            self.parameterService.getMapObjectBehaviorCloudMovementSpeed()
        )
        self.fireBehavior = FireBehavior(
            self.mapLayerCellService,
            self.fireGenerator,
            self.smokeGenerator,
            self.parameterService.getMapObjectBehaviorFireBurningTime(),
            self.parameterService.getMapObjectBehaviorFireDistributionTime()
        )
        self.helicopterBehavior = HelicopterBehavior(
            self.mapLayerCellService,
            self.fireBehavior
        )
        self.smokeBehavior = SmokeBehavior(
            self.mapLayerCellService,
            self.parameterService.getMapObjectGeneratorSmokeLifeTime()
        )

        ### MAP GENERATORS ###
        self.mainMapGenerator = MainMapGenerator(
            self.mapLayerService,
            self.cloudGenerator,
            self.earthGenerator,
            self.fireGenerator,
            self.grassGenerator,
            self.helicopterGenerator,
            self.hospitalGenerator,
            self.rockGenerator,
            self.shopGenerator,
            self.treeGenerator,
            self.waterGenerator,
            self.cloudBehavior,
            self.fireBehavior,
            self.smokeBehavior,
            self.helicopterBehavior,
            self.parameterService.getMapRowsCount(),
            self.parameterService.getMapColsCount(),
            self.parameterService.getMapObjectGeneratorWaterPercent(),
            self.parameterService.getMapObjectGeneratorRockPercent(),
            self.parameterService.getMapObjectGeneratorTotalTreePercent(),
            self.parameterService.getMapObjectGeneratorSingleTreePercent(),
            self.parameterService.getMapObjectGeneratorBurningTreePercent(),
            self.parameterService.getMapObjectGeneratorEarthPercent(),
            self.parameterService.getMapObjectGeneratorNormalCloudPercent(),
            self.parameterService.getMapObjectGeneratorLightningCloudPercent(),
            self.parameterService.getMapObjectGeneratorRainingCloudPercent(),
            self.parameterService.getMapObjectGeneratorRainbowCloudPercent()
        )

        # Main ###
        dispatcher.send(signal=PreLoadService.NAME, sender=None,
                        data={"event": PreLoadService("initialize main services")})
        self.mainSceneGenerator = MainSceneGenerator(self.mainMapGenerator)
        self.playerService = PlayerService(
            self.helicopterBehavior,
            self.parameterService.getGameExtinguishedFireScore(),
            self.parameterService.getGameNotExtinguishedFireScore(),
            self.parameterService.getGameHelicopterUpgradeCost(),
            self.parameterService.getGameHelicopterUpgradeCostMultiplicator(),
            self.parameterService.getGameHelicopterHealCost()
        )
        self.keyboardControllerService = KeyboardControllerService()

        ### Subscribers ###
        self.helicopterEventSubscriber = PlayerEventSubscriber(self.playerService)
        self.helicopterEventSubscriber.subscribe()
