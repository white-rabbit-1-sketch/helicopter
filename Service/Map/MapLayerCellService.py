from typing import Union, Type
from pydispatch import dispatcher

from game.Entity.MapLayerCell import MapLayerCell
from game.Entity.MapObject.AbstractMapObject import AbstractMapObject
from game.Event.Map.Object.ObjectEnterPlace import ObjectEnterPlace

class MapLayerCellService:
    def setCellObject(self, targetCell: MapLayerCell, object: Union[AbstractMapObject, None]) -> None:
        targetCell.object = object

        if object:
            currentCell = object.cell
            object.cell = targetCell

            if currentCell and not currentCell == targetCell:
                currentCell.object = None

                dispatcher.send(signal=ObjectEnterPlace.NAME, sender=None, data={"event": ObjectEnterPlace(object)})

    def getCellCollisionByObjectType(
            self, cell: MapLayerCell,
            objectType: Type[AbstractMapObject]
    ) -> Union[AbstractMapObject, None]:
        result = None

        for layerName, layer in cell.layer.map.layers.items():
            layerCell = layer.getCellByPosition(cell.x, cell.y)

            if not layerCell.object or not isinstance(layerCell.object, objectType): continue

            result = layerCell.object

            break

        return result