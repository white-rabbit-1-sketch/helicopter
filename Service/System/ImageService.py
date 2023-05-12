import pygame
from PIL import Image as PilImage, ImageSequence
from typing import List
from pygame import Surface
import os

from game.Entity.Image import Image

class ImageService:
    IMAGE_FORMAT_GIF = 'GIF'
    FRAME_TYPE_RGBA = 'RGBA'

    def __init__(self) -> None:
        self.imageSurfaceMap = {}

    def getImageFrameSurfaceList(self, imagePath: str) -> List[Surface]:
        result = []

        pilImage = PilImage.open(imagePath)
        if pilImage.format == self.IMAGE_FORMAT_GIF and pilImage.is_animated:
            for frame in ImageSequence.Iterator(pilImage):
                result.append(self.convertPilImageToSurface(frame.convert(self.FRAME_TYPE_RGBA)))
        else:
            result.append(self.convertPilImageToSurface(pilImage))

        return result

    def convertPilImageToSurface(self, pilImage) -> Surface:
        return pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert_alpha()

    def scaleImageSurface(self, imageSurface: Surface, width: int, height: int):
        return pygame.transform.scale(imageSurface, (width, height))

    def scaleImageSurfaceList(self, imageSurfaceList: List[Surface], width: int, height: int) -> list:
        result = []

        for imageSurface in imageSurfaceList:
            result.append(self.scaleImageSurface(imageSurface, width, height))

        return result

    def buildImage(self, path: str, width: int, height: int) -> Image:
        imageFrameSurfaceList = self.getImageFrameSurfaceList(path)
        imageFrameSurfaceList = self.scaleImageSurfaceList(
            imageFrameSurfaceList,
            width,
            height
        )

        self.imageSurfaceMap[path] = imageFrameSurfaceList

        image = Image(path)

        return image

    def buildImageList(self, path: str, width: int, height: int) -> List[Image]:
        result = []

        for fileName in os.listdir(path):
            result.append(self.buildImage("%s%s" % (path, fileName), width, height))

        return result

