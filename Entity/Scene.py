from helicopter.Entity.Map import Map
from helicopter.Entity.Player import Player

class Scene:
    def __init__(
        self,
        map: Map,
        player: Player
    ) -> None:
        self.map = map
        self.player = player