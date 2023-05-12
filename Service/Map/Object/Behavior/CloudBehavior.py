import time

from game.Service.Map.Object.Behavior.AbstractObjectBehavior import AbstractObjectBehavior
from game.Entity.MapObject.Cloud.AbstractCloud import AbstractCloud
from game.Service.Map.MapLayerCellService import MapLayerCellService

class CloudBehavior(AbstractObjectBehavior):
    def __init__(
        self,
        mapLayerCellService: MapLayerCellService,
        cloudMovementSpeed: int
    ) -> None:
        AbstractObjectBehavior.__init__(self, mapLayerCellService)

        self.cloudMovementSpeed = cloudMovementSpeed

    def handleCloud(self, cloud: AbstractCloud) -> None:
        currentTime = time.time()

        if not cloud.lastMovementTime or currentTime - cloud.lastMovementTime >= self.cloudMovementSpeed:
            currentCloudCell = cloud.cell

            self.mapLayerCellService.setCellObject(cloud.cell, None)

            targetCloudCell = currentCloudCell.layer.getCellByPosition(
                currentCloudCell.x - 1 if currentCloudCell.x > 0 else currentCloudCell.layer.map.colsCount - 1,
                currentCloudCell.y
            )
            self.mapLayerCellService.setCellObject(targetCloudCell, cloud)
            cloud.lastMovementTime = currentTime