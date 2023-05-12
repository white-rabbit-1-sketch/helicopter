from pydispatch import dispatcher

from game.Entity.Player import Player
from game.Service.Map.Object.Behavior.HelicopterBehavior import HelicopterBehavior
from game.Event.GameOver import GameOver

class PlayerService:
    def __init__(
        self,
        helicopterBehavior: HelicopterBehavior,
        extinguishedFireScore: int,
        notExtinguishedFireScore: int,
        helicopterUpgradeCost: int,
        helicopterUpgradeCostMultiplicator: float,
        helicopterHealCost: int
    ) -> None:
        self.helicopterBehavior = helicopterBehavior
        self.extinguishedFireScore = extinguishedFireScore
        self.notExtinguishedFireScore = notExtinguishedFireScore
        self.helicopterUpgradeCost = helicopterUpgradeCost
        self.helicopterUpgradeCostMultiplicator = helicopterUpgradeCostMultiplicator
        self.helicopterHealCost = helicopterHealCost

    def playerMoveUp(self, player: Player) -> None:
        if self.helicopterBehavior.canHelicopterMove(player.helicopter):
            self.helicopterBehavior.moveHelicopterUp(player.helicopter)

    def playerMoveDown(self, player: Player) -> None:
        if self.helicopterBehavior.canHelicopterMove(player.helicopter):
            self.helicopterBehavior.moveHelicopterDown(player.helicopter)

    def playerMoveLeft(self, player: Player) -> None:
        if self.helicopterBehavior.canHelicopterMove(player.helicopter):
            self.helicopterBehavior.moveHelicopterLeft(player.helicopter)

    def playerMoveRight(self, player: Player) -> None:
        if self.helicopterBehavior.canHelicopterMove(player.helicopter):
            self.helicopterBehavior.moveHelicopterRight(player.helicopter)

    def playerAction(self, player: Player) -> None:
        if self.helicopterBehavior.canHelicopterGrabWater(player.helicopter):
            self.helicopterBehavior.grabWaterByHelicopter(player.helicopter)

        if self.helicopterBehavior.canHelicopterExtinguishFire(player.helicopter):
            self.playerHelicopterExtinguishFire(player)

        if self.helicopterBehavior.canHelicopterUpgrade(player.helicopter):
            self.playerHelicopterUpgrade(player)

        if self.helicopterBehavior.canHelicopterHeal(player.helicopter):
            self.playerHelicopterHeal(player)

    def playerHelicopterUpgrade(self, player: Player) -> None:
        upgradeCost = int(player.helicopter.waterCapacity * self.helicopterUpgradeCostMultiplicator * self.helicopterUpgradeCost)

        if upgradeCost <= player.score:
            self.helicopterBehavior.upgradeHelicopter(player.helicopter)
            player.score -= upgradeCost

    def playerHelicopterHeal(self, player: Player) -> None:
        if self.helicopterHealCost <= player.score:
            self.helicopterBehavior.healHelicopter(player.helicopter)
            player.score -= self.helicopterHealCost

    def playerHelicopterExtinguishFire(self, player: Player) -> None:
        self.helicopterBehavior.extinguishFireByHelicopter(player.helicopter)
        player.score += self.extinguishedFireScore
        player.extinguishedFiresCount += 1

    def onFireDestroyTree(self, player: Player) -> None:
        player.score += self.notExtinguishedFireScore
        player.notExtinguishedFiresCount += 1

        if player.score < 0: player.score = 0

    def onHelicopterDestroyed(self, player: Player) -> None:
        dispatcher.send(signal=GameOver.NAME, sender=None, data={"event": GameOver(player.scene)})


