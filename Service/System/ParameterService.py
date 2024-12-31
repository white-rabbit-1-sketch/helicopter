import configparser

class ParameterService:
    MAP_SECTION = "MAP"
    MAP_OBJECT_GENERATOR_SECTION = "MAP-OBJECT-GENERATOR"
    MAP_OBJECT_BEHAVIOR_SECTION = "MAP-OBJECT-BEHAVIOR"
    MAP_RESOURCE_SECTION = "MAP-RESOURCE"
    INTERFACE_RESOURCE_SECTION = "INTERFACE-RESOURCE"
    OBJECT_SETTINGS = "OBJECT-SETTINGS"
    SCREEN_SECTION = "SCREEN"
    GAME_SECTION = "GAME"

    def __init__(self, parametersFilePath: str):
        self.parameterContainer = configparser.ConfigParser()
        self.parameterContainer.read(parametersFilePath)

    def getMapImageDirectoryGrass(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'GRASS')

    def getMapImageDirectoryWater(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'WATER')

    def getMapImageDirectoryRocks(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'ROCKS')

    def getMapImageDirectoryTrees(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'TREES')

    def getMapImageDirectoryFires(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'FIRES')

    def getMapImageDirectoryEarth(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'EARTH')

    def getMapImageDirectoryShops(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'SHOPS')

    def getMapImageDirectoryHospitals(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'HOSPITALS')

    def getMapImageDirectoryCloudsNormal(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'CLOUDS_NORMAL')

    def getMapImageDirectoryCloudsLightning(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'CLOUDS_LIGHTNING')

    def getMapImageDirectoryCloudsRaining(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'CLOUDS_RAINING')

    def getMapImageDirectoryCloudsRainbow(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'CLOUDS_RAINBOW')

    def getMapImageDirectoryWalls(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'WALLS')

    def getMapImageDirectorySmoke(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'SMOKE')

    def getMapImageDirectoryHelicopters(self) -> str:
        return self.parameterContainer.get(self.MAP_RESOURCE_SECTION, 'HELICOPTERS')

    def getInterfaceImageHealthIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'HEALTH_ICON')

    def getInterfaceImageHealthIconWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'HEALTH_ICON_WIDTH')

    def getInterfaceImageHealthHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'HEALTH_ICON_HEIGHT')

    def getInterfaceImageTrophyIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'TROPHY_ICON')

    def getInterfaceImageTrophyIconWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'TROPHY_ICON_WIDTH')

    def getInterfaceImageTrophyHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'TROPHY_ICON_HEIGHT')

    def getInterfaceImageWaterIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'WATER_ICON')

    def getInterfaceImageWaterIconWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'WATER_ICON_WIDTH')

    def getInterfaceImageWaterHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'WATER_ICON_HEIGHT')

    def getInterfaceImagePaleHealthIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'PALE_HEALTH_ICON')

    def getInterfaceImagePaleHealthWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'PALE_HEALTH_ICON_WIDTH')

    def getInterfaceImagePaleHealthHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'PALE_HEALTH_ICON_HEIGHT')

    def getInterfaceImagePaleWaterIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'PALE_WATER_ICON')

    def getInterfaceImagePaleWaterWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'PALE_WATER_ICON_WIDTH')

    def getInterfaceImagePaleWaterHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'PALE_WATER_ICON_HEIGHT')

    def getInterfaceImageFireIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'FIRE_ICON')

    def getInterfaceImageFireWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'FIRE_ICON_WIDTH')

    def getInterfaceImageFireHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'FIRE_ICON_HEIGHT')

    def getInterfaceImageExtinguishedFireIcon(self) -> str:
        return self.parameterContainer.get(self.INTERFACE_RESOURCE_SECTION, 'EXTINGUISHED_FIRE_ICON')

    def getInterfaceImageExtinguishedFireWidth(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'EXTINGUISHED_FIRE_ICON_WIDTH')

    def getInterfaceImageExtinguishedFireHeight(self) -> int:
        return self.parameterContainer.getint(self.INTERFACE_RESOURCE_SECTION, 'EXTINGUISHED_FIRE_ICON_HEIGHT')

    def getMapRowsCount(self) -> int:
        return self.parameterContainer.getint(self.MAP_SECTION, 'ROWS_COUNT')

    def getMapColsCount(self) -> int:
        return self.parameterContainer.getint(self.MAP_SECTION, 'COLS_COUNT')

    def getMapObjectGeneratorWaterPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'WATER_PERCENT')

    def getMapObjectGeneratorRockPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'ROCK_PERCENT')

    def getMapObjectGeneratorTotalTreePercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'TOTAL_TREE_PERCENT')

    def getMapObjectGeneratorSingleTreePercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'SINGLE_TREE_PERCENT')

    def getMapObjectGeneratorEarthPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'EARTH_PERCENT')

    def getMapObjectGeneratorBurningTreePercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'BURNING_TREE_PERCENT')

    def getMapObjectGeneratorSmokeLifeTime(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'SMOKE_LIFE_TIME')

    def getMapObjectBehaviorFireBurningTime(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_BEHAVIOR_SECTION, 'FIRE_BURNING_TIME')

    def getMapObjectBehaviorFireDistributionTime(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_BEHAVIOR_SECTION, 'FIRE_DISTRIBUTION_TIME')

    def getMapObjectGeneratorNormalCloudPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'NORMAL_CLOUD_PERCENT')

    def getMapObjectGeneratorLightningCloudPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'LIGHTNING_CLOUD_PERCENT')

    def getMapObjectGeneratorRainingCloudPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'RAINING_CLOUD_PERCENT')

    def getMapObjectGeneratorRainbowCloudPercent(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_GENERATOR_SECTION, 'RAINBOW_CLOUD_PERCENT')

    def getMapObjectBehaviorCloudMovementSpeed(self) -> int:
        return self.parameterContainer.getint(self.MAP_OBJECT_BEHAVIOR_SECTION, 'CLOUD_MOVEMENT_SPEED')

    def getObjectSettingsHelicopterWaterCapacity(self) -> int:
        return self.parameterContainer.getint(self.OBJECT_SETTINGS, 'HELICOPTER_WATER_CAPACITY')

    def getObjectSettingsHelicopterMaxWaterCapacity(self) -> int:
        return self.parameterContainer.getint(self.OBJECT_SETTINGS, 'HELICOPTER_MAX_WATER_CAPACITY')

    def getObjectSettingsHelicopterMaxHealth(self) -> int:
        return self.parameterContainer.getint(self.OBJECT_SETTINGS, 'HELICOPTER_MAX_HEALTH')

    def getObjectSettingsHelicopterMoveSpeed(self) -> float:
        return self.parameterContainer.getfloat(self.OBJECT_SETTINGS, 'HELICOPTER_MOVE_SPEED')

    def getScreenWidth(self) -> int:
        return self.parameterContainer.getint(self.SCREEN_SECTION, 'WIDTH')

    def getScreenHeight(self) -> int:
        return self.parameterContainer.getint(self.SCREEN_SECTION, 'HEIGHT')

    def getScreenFps(self) -> int:
        return self.parameterContainer.getint(self.SCREEN_SECTION, 'FPS')

    def getScreenAnimationSpeed(self) -> int:
        return self.parameterContainer.getint(self.SCREEN_SECTION, 'ANIMATION_SPEED')

    def getScreenWindowCaption(self) -> str:
        return self.parameterContainer.get(self.SCREEN_SECTION, 'WINDOW_CAPTION')

    def getScreenMapObjectWidth(self) -> int:
        return self.parameterContainer.getint(self.MAP_SECTION, 'MAP_OBJECT_WIDTH')

    def getScreenMapObjectHeight(self) -> int:
        return self.parameterContainer.getint(self.MAP_SECTION, 'MAP_OBJECT_HEIGHT')

    def getGameExtinguishedFireScore(self) -> int:
        return self.parameterContainer.getint(self.GAME_SECTION, 'EXTINGUISHED_FIRE_SCORE')

    def getGameNotExtinguishedFireScore(self) -> int:
        return self.parameterContainer.getint(self.GAME_SECTION, 'NOT_EXTINGUISHED_FIRE_SCORE')

    def getGameHelicopterUpgradeCost(self) -> int:
        return self.parameterContainer.getint(self.GAME_SECTION, 'HELICOPTER_UPGRADE_COST')

    def getGameHelicopterUpgradeCostMultiplicator(self) -> float:
        return self.parameterContainer.getfloat(self.GAME_SECTION, 'HELICOPTER_UPGRADE_COST_MULTIPLICATOR')

    def getGameHelicopterHealCost(self) -> int:
        return self.parameterContainer.getint(self.GAME_SECTION, 'HELICOPTER_HEAL_COST')

    def getGameSavePath(self) -> int:
        return self.parameterContainer.get(self.GAME_SECTION, 'SAVE_PATH')