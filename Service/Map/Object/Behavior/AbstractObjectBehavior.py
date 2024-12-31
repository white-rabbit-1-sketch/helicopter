from abc import ABC

from helicopter.Service.Map.MapLayerCellService import MapLayerCellService

class AbstractObjectBehavior(ABC):
    def __init__(self,
        mapLayerCellService: MapLayerCellService,
    ) -> None:
        self.mapLayerCellService = mapLayerCellService