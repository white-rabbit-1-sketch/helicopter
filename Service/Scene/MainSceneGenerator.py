from game.Entity.Scene import Scene
from game.Entity.Player import Player
from game.Service.Map.Level.MainMapGenerator import MainMapGenerator

class MainSceneGenerator:
    def __init__(
            self,
            mainMapGenerator: MainMapGenerator
    ) -> None:
        self.mainMapGenerator = mainMapGenerator

    def generateScene(self) -> Scene:
        map = self.mainMapGenerator.generateMap()
        player = Player(self.mainMapGenerator.createHelicopterOnMap(map))

        scene = Scene(map, player)
        player.scene = scene
        map.scene = scene

        return scene

    def handleScene(self, scene: Scene) -> None:
        self.mainMapGenerator.handleBehavior(scene.map)