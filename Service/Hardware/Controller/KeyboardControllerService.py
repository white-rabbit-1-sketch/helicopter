import pygame
import threading
from typing import Callable
from pydispatch import dispatcher

from helicopter.Entity.Scene import Scene
from helicopter.Event.PlayerMoveUp import PlayerMoveUp
from helicopter.Event.PlayerMoveDown import PlayerMoveDown
from helicopter.Event.PlayerMoveLeft import PlayerMoveLeft
from helicopter.Event.PlayerMoveRight import PlayerMoveRight
from helicopter.Event.PlayerAction import PlayerAction
from helicopter.Event.GameQuit import GameQuit
from helicopter.Event.GameSave import GameSave
from helicopter.Event.GameLoad import GameLoad
from helicopter.Event.GameNew import GameNew

class KeyboardControllerService:
    def __init__(self) -> None:
        self.scene = None
        self.keyReceiver = None
        self.thread = None
        self.stopFlag = threading.Event()

    def listen(self, scene: Scene, keyReceiver: Callable) -> None:
        self.scene = scene
        self.keyReceiver = keyReceiver
        self.thread = threading.Thread(target=self.startListener, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.stopFlag.set()

    def startListener(self) -> None:
        while not self.stopFlag.is_set():
            for c in self.keyReceiver():
                if c == ord("q"):
                    dispatcher.send(signal=GameQuit.NAME, sender=None, data={"event": GameQuit()})
                elif c == ord("s"):
                    dispatcher.send(signal=GameSave.NAME, sender=None, data={"event": GameSave(self.scene)})
                elif c == ord("l"):
                    dispatcher.send(signal=GameLoad.NAME, sender=None, data={"event": GameLoad()})
                elif c == ord("n"):
                    dispatcher.send(signal=GameNew.NAME, sender=None, data={"event": GameNew()})
                elif c == pygame.K_UP:
                    dispatcher.send(signal=PlayerMoveUp.NAME, sender=None, data={"event": PlayerMoveUp(self.scene)})
                elif c == pygame.K_DOWN:
                    dispatcher.send(signal=PlayerMoveDown.NAME, sender=None, data={"event": PlayerMoveDown(self.scene)})
                elif c == pygame.K_LEFT:
                    dispatcher.send(signal=PlayerMoveLeft.NAME, sender=None, data={"event": PlayerMoveLeft(self.scene)})
                elif c == pygame.K_RIGHT:
                    dispatcher.send(signal=PlayerMoveRight.NAME, sender=None, data={"event": PlayerMoveRight(self.scene)})
                elif c == pygame.K_SPACE:
                    dispatcher.send(signal=PlayerAction.NAME, sender=None, data={"event": PlayerAction(self.scene)})
