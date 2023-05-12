from __future__ import annotations
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from game.Entity.Scene import Scene

from game.Entity.MapObject.Helicopter import Helicopter

class Player:
    def __init__(
        self,
        helicopter: Helicopter
    ) -> None:
        self.scene: Union[Scene, None] = None
        self.helicopter = helicopter
        self.score: int = 0
        self.notExtinguishedFiresCount = 0
        self.extinguishedFiresCount = 0