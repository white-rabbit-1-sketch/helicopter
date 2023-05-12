from game.Entity.Map import Map
from game.Entity.Player import Player

class Scene:
    def __init__(
        self,
        map: Map,
        player: Player
    ) -> None:
        self.map = map
        self.player = player