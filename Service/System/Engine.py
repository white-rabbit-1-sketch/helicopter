import pygame
import pickle
from pydispatch import dispatcher

from helicopter.Service.System.ParameterService import ParameterService
from helicopter.Service.Scene.MainSceneGenerator import MainSceneGenerator
from helicopter.Service.Hardware.Renderer.OpenGLRenderer import OpenGLRenderer
from helicopter.Service.Hardware.Controller.KeyboardControllerService import KeyboardControllerService
from helicopter.Event.GameQuit import GameQuit
from helicopter.Event.GameOver import GameOver
from helicopter.Event.GameNew import GameNew
from helicopter.Event.GameLoad import GameLoad
from helicopter.Event.GameSave import GameSave
from helicopter.Service.Map.MapLayerService import MapLayerService

class Engine:
    def __init__(
        self,
        parameterService: ParameterService,
        openGLRenderer: OpenGLRenderer,
        keyboardControllerService: KeyboardControllerService,
        mainSceneGenerator: MainSceneGenerator,
        mapLayerService: MapLayerService,
    ):
        self.parameterService = parameterService
        self.openGLRenderer = openGLRenderer
        self.keyboardControllerService = keyboardControllerService
        self.mainSceneGenerator = mainSceneGenerator
        self.mapLayerService = mapLayerService

        self.fps = self.parameterService.getScreenFps()
        self.clock = pygame.time.Clock()
        self.tick = 0

        self.scene = None

        self.sigTermReceived = False
        self.gameOver = False
        self.needToSaveGame = False
        self.needToLoadGame = False
        self.needToCreateNewGame = False


    def subscribe(self) -> None:
        dispatcher.connect(self.onGameQuit, signal=GameQuit.NAME)
        dispatcher.connect(self.onGameOver, signal=GameOver.NAME)
        dispatcher.connect(self.onGameNew, signal=GameNew.NAME)
        dispatcher.connect(self.onGameLoad, signal=GameLoad.NAME)
        dispatcher.connect(self.onGameSave, signal=GameSave.NAME)

    def run(self) -> None:
        self.subscribe()
        self.createNewGame()
        self.keyboardControllerService.listen(self.scene, self.openGLRenderer.getPressedKeyGenerator)

        self.clock.tick(self.fps)
        while True:
            if self.sigTermReceived: break
            if self.needToSaveGame: self.saveGame()
            if self.needToLoadGame: self.loadGame()
            if self.needToCreateNewGame: self.createNewGame()

            self.tick += 1
            if not self.gameOver:
                self.openGLRenderer.handleEvents()
                self.openGLRenderer.renderScene(self.scene, self.tick)
                self.mainSceneGenerator.handleScene(self.scene)

            if self.gameOver: self.openGLRenderer.renderGameOverScreen(self.scene, self.tick)
            # Create new game or load save

            self.clock.tick(self.fps)

        self.keyboardControllerService.stop()
        self.openGLRenderer.stop()

    def onGameNew(self, sender, **kwargs) -> None:
        if not self.needToLoadGame and not self.needToSaveGame and not self.needToCreateNewGame:
            self.needToCreateNewGame = True

    def createNewGame(self):
        self.openGLRenderer.renderBlackScreen("Creating new helicopter...")
        self.scene = self.mainSceneGenerator.generateScene()
        self.keyboardControllerService.scene = self.scene
        self.gameOver = False
        self.needToCreateNewGame = False

    def onGameSave(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: GameSave = data.get('event')

        if not self.gameOver and not self.needToLoadGame and not self.needToSaveGame and not self.needToCreateNewGame:
            self.needToSaveGame = True

    def saveGame(self) -> None:
        self.openGLRenderer.renderBlackScreen("Saving helicopter...")
        with open(self.parameterService.getGameSavePath(), "wb") as f:
            pickle.dump(self.scene, f)
        self.keyboardControllerService.scene = self.scene
        self.needToSaveGame = False

    def onGameLoad(self, sender, **kwargs) -> None:
        self.openGLRenderer.renderBlackScreen("Loading helicopter...")
        if not self.needToSaveGame and not self.needToLoadGame and not self.needToCreateNewGame: self.needToLoadGame = True

    def loadGame(self) -> None:
        with open(self.parameterService.getGameSavePath(), "rb") as f:
            self.scene = pickle.load(f)
        self.mapLayerService.initNearestCells(self.scene.map)
        self.keyboardControllerService.scene = self.scene
        self.needToLoadGame = False
        self.gameOver = False

    def onGameQuit(self, sender, **kwargs) -> None:
        self.sigTermReceived = True

    def onGameOver(self, sender, **kwargs) -> None:
        self.gameOver = True