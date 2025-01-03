from pydispatch import dispatcher

from helicopter.Service.Player.PlayerService import PlayerService
from helicopter.Event.PlayerMoveUp import PlayerMoveUp
from helicopter.Event.PlayerMoveDown import PlayerMoveDown
from helicopter.Event.PlayerMoveLeft import PlayerMoveLeft
from helicopter.Event.PlayerMoveRight import PlayerMoveRight
from helicopter.Event.PlayerAction import PlayerAction
from helicopter.Event.Map.Object.HelicopterDestroyed import HelicopterDestroyed
from helicopter.Event.Map.Object.FireDestroyImpactObject import FireDestroyImpactObject

class PlayerEventSubscriber:
    def __init__(self, playerService: PlayerService) -> None:
        self.playerService = playerService

    def subscribe(self) -> None:
        dispatcher.connect(self.onPlayerMoveUp, signal=PlayerMoveUp.NAME)
        dispatcher.connect(self.onPlayerMoveDown, signal=PlayerMoveDown.NAME)
        dispatcher.connect(self.onPlayerMoveLeft, signal=PlayerMoveLeft.NAME)
        dispatcher.connect(self.onPlayerMoveRight, signal=PlayerMoveRight.NAME)
        dispatcher.connect(self.onPlayerAction, signal=PlayerAction.NAME)
        dispatcher.connect(self.onFireDestroyImpactObject, signal=FireDestroyImpactObject.NAME)
        dispatcher.connect(self.onHelicopterDestroyed, signal=HelicopterDestroyed.NAME)

    def onPlayerMoveUp(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: PlayerMoveUp = data.get('event')

        self.playerService.playerMoveUp(event.scene.player)

    def onPlayerMoveDown(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: PlayerMoveUp = data.get('event')

        self.playerService.playerMoveDown(event.scene.player)

    def onPlayerMoveLeft(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: PlayerMoveUp = data.get('event')

        self.playerService.playerMoveLeft(event.scene.player)

    def onPlayerMoveRight(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: PlayerMoveUp = data.get('event')

        self.playerService.playerMoveRight(event.scene.player)

    def onPlayerAction(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: PlayerAction = data.get('event')

        self.playerService.playerAction(event.scene.player)

    def onFireDestroyImpactObject(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: FireDestroyImpactObject = data.get('event')

        self.playerService.onFireDestroyTree(event.object.cell.layer.map.scene.player)

    def onHelicopterDestroyed(self, sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: HelicopterDestroyed = data.get('event')

        self.playerService.onHelicopterDestroyed(event.helicopter.cell.layer.map.scene.player)

