from abc import ABC

from game.Service.Map.MapLayerCellService import MapLayerCellService

class AbstractObjectBehavior(ABC):
    def __init__(self,
        mapLayerCellService: MapLayerCellService,
    ) -> None:
        self.mapLayerCellService = mapLayerCellService