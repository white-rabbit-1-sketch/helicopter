import pygame
import time
from pygame import Surface
from typing import Union
from pydispatch import dispatcher

from game.Entity.Scene import Scene
from game.Entity.Image import Image
from game.Service.System.ImageService import ImageService
from game.Event.GameQuit import GameQuit

class OpenGLRenderer:
    ELEMENTS_PADDING = 5

    def __init__(
            self,
            imageService: ImageService,
            windowCaption: str,
            screenWidth: int,
            screenHeight: int,
            fps: int,
            animationSpeed: int,
            mapObjectWidth: int,
            mapObjectHeight: int,
    ) -> None:
        self.imageService = imageService
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.mapObjectWidth = mapObjectWidth
        self.mapObjectHeight = mapObjectHeight
        self.fps = fps
        self.animationSpeed = animationSpeed
        self.healthIconImage: Union[Image, None] = None
        self.trophyIconImage: Union[Image, None] = None
        self.waterIconImage: Union[Image, None] = None
        self.fireIconImage: Union[Image, None] = None
        self.extinguishedFireIconImage: Union[Image, None] = None
        self.paleHealthIconImage: Union[Image, None] = None
        self.paleWaterIconImage: Union[Image, None] = None

        pygame.init()
        pygame.display.set_caption(windowCaption)
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

    def buildProgressBarBlock(
            self,
            tick: int,
            maxValue: int,
            currentValue: int,
            filledIconImage: Image,
            unfilledIconImage: Image
    ) -> Surface:
        elementsWidth = 0
        elementsMaxHeight = 0
        iconFrameSurfaceList = []
        for i in range(maxValue):
            iconImage = filledIconImage if not (i > currentValue - 1) else unfilledIconImage

            iconFrameSurface = self.imageService.imageSurfaceMap[iconImage.path][(tick // (self.fps // self.animationSpeed)) % len(self.imageService.imageSurfaceMap[iconImage.path])]
            iconFrameSurfaceRect = iconFrameSurface.get_rect()

            iconFrameSurfaceList.append(iconFrameSurface)

            elementsWidth += iconFrameSurfaceRect.width
            if i > 0 and i < maxValue:
                elementsWidth += self.ELEMENTS_PADDING

            if iconFrameSurfaceRect.height > elementsMaxHeight:
                elementsMaxHeight = iconFrameSurfaceRect.height

        progressBarBlock = pygame.Surface((elementsWidth, elementsMaxHeight))
        progressBarBlock.fill((0, 0, 0))

        for i, iconFrameSurface in enumerate(iconFrameSurfaceList):
            x = iconFrameSurface.get_rect().width

            if i > 0 and i < len(iconFrameSurfaceList):
                x += self.ELEMENTS_PADDING

            x *= i

            progressBarBlock.blit(iconFrameSurface, (x, 0))

        return progressBarBlock

    def buildPlayerIconTextBlock(
            self,
            tick: int,
            iconImage: Image,
            text: str
    ) -> Surface:
        iconFrameSurface = self.imageService.imageSurfaceMap[iconImage.path][(tick // (self.fps // self.animationSpeed)) % len(self.imageService.imageSurfaceMap[iconImage.path])]
        iconFrameSurfaceRect = iconFrameSurface.get_rect()

        font = pygame.font.SysFont(None, 32)
        textSurface = font.render(text, True, (255, 255, 255))
        textSurfaceRect = textSurface.get_rect()

        elementsWidth = iconFrameSurfaceRect.width + textSurfaceRect.width + self.ELEMENTS_PADDING
        elementsMaxHeight = max(iconFrameSurfaceRect.height, textSurfaceRect.height)

        iconTextBlock = pygame.Surface((elementsWidth, elementsMaxHeight))
        iconTextBlock.fill((0, 0, 0))

        iconTextBlock.blit(iconFrameSurface, (0, 0))
        iconTextBlock.blit(textSurface, (iconFrameSurfaceRect.width + self.ELEMENTS_PADDING, 0))

        return iconTextBlock

    def buildPlayerStatisticsBlock(self, scene: Scene, tick: int) -> Surface:
        healthBlock = self.buildPlayerIconTextBlock(tick, self.healthIconImage, "%s/%s" % (scene.player.helicopter.getCurrentHealth(), scene.player.helicopter.getMaxHealth()))
        waterCargoBlock = self.buildPlayerIconTextBlock(tick, self.waterIconImage, "%s/%s" % (scene.player.helicopter.getWaterVolume(), scene.player.helicopter.getWaterCapacity()))
        scoreBlock = self.buildPlayerIconTextBlock(tick, self.trophyIconImage, str(scene.player.score))
        extinguishedFiresBlock = self.buildPlayerIconTextBlock(tick, self.extinguishedFireIconImage, str(scene.player.extinguishedFiresCount))
        notExtinguishedFiresBlock = self.buildPlayerIconTextBlock(tick, self.fireIconImage, str(scene.player.notExtinguishedFiresCount))

        elementsMaxHeight = max(
            healthBlock.get_rect().height,
            scoreBlock.get_rect().height,
            extinguishedFiresBlock.get_rect().height,
            notExtinguishedFiresBlock.get_rect().height,
        )

        statisticsBlock = pygame.Surface((self.screenWidth, elementsMaxHeight + self.ELEMENTS_PADDING * 2))
        statisticsBlock.fill((0, 0, 0))

        # Left
        statisticsBlock.blit(healthBlock, (self.ELEMENTS_PADDING, self.ELEMENTS_PADDING))
        statisticsBlock.blit(waterCargoBlock, (
            healthBlock.get_rect().width + self.ELEMENTS_PADDING * 2,
            self.ELEMENTS_PADDING
        ))

        # Center
        font = pygame.font.SysFont(None, 32)
        optionsBlock = font.render("[N]ew game   [L]oad   [S]ave   [Q]uit   [SPACE]Action", True, (255, 255, 255))

        statisticsBlock.blit(optionsBlock, ((statisticsBlock.get_rect().width // 2) - optionsBlock.get_rect().width / 2, self.ELEMENTS_PADDING))

        # Right
        statisticsBlock.blit(
            scoreBlock,
            (
                statisticsBlock.get_rect().width - scoreBlock.get_rect().width - self.ELEMENTS_PADDING,
                self.ELEMENTS_PADDING
            )
        )
        statisticsBlock.blit(
            extinguishedFiresBlock,
            (
                statisticsBlock.get_rect().width - scoreBlock.get_rect().width - self.ELEMENTS_PADDING - extinguishedFiresBlock.get_rect().width - self.ELEMENTS_PADDING,
                self.ELEMENTS_PADDING
            )
        )
        statisticsBlock.blit(
            notExtinguishedFiresBlock,
            (
                statisticsBlock.get_rect().width - scoreBlock.get_rect().width - self.ELEMENTS_PADDING - extinguishedFiresBlock.get_rect().width - self.ELEMENTS_PADDING - notExtinguishedFiresBlock.get_rect().width - self.ELEMENTS_PADDING,
                self.ELEMENTS_PADDING
            )
        )

        return statisticsBlock

    def renderScene(self, scene: Scene, tick: int) -> None:
        self.screen.fill((0, 0, 0))

        """for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.screenWidth = event.w
                self.screenHeight = event.h"""

        contentBlock = pygame.Surface(self.screen.get_size())
        contentBlock.fill((0, 0, 0))

        playerStatisticsBlock = self.buildPlayerStatisticsBlock(scene, tick)
        contentBlock.blit(playerStatisticsBlock, (0, 0))

        for x, y in scene.map.getCordsGenerator():
            for layerName, layer in scene.map.layers.items():
                cell = layer.getCellByPosition(x, y)

                if not cell.object: continue

                imageFrameSurface = self.imageService.imageSurfaceMap[cell.object.getImage().path][(tick // (self.fps // self.animationSpeed)) % len(self.imageService.imageSurfaceMap[cell.object.getImage().path])]
                imageFrameSurfaceRect = imageFrameSurface.get_rect()

                contentBlock.blit(
                    imageFrameSurface.subsurface(imageFrameSurfaceRect),
                    (x * self.mapObjectWidth, playerStatisticsBlock.get_rect().bottom + y * self.mapObjectHeight)
                )

        self.screen.blit(contentBlock, (0, 0))

        pygame.display.flip()

    def renderGameOverScreen(self, scene: Scene, tick: int) -> None:
        self.screen.fill((0, 0, 0))

        contentBlock = pygame.Surface(self.screen.get_size())
        contentBlock.fill((0, 0, 0))

        font = pygame.font.SysFont(None, 48)
        gamOverTextSurface = font.render("Game over", True, (255, 255, 255))
        gameOverTextSurfaceRect = gamOverTextSurface.get_rect()
        #textRect.center = (self.screenWidth // 2, self.screenHeight // 2)
        contentBlock.blit(gamOverTextSurface, (self.screenWidth // 2 - gameOverTextSurfaceRect.width / 2, self.screenHeight // 2))
        contentBlock.blit(
            gamOverTextSurface,
            (self.screenWidth // 2 - gameOverTextSurfaceRect.width / 2, self.screenHeight // 2)
        )

        font = pygame.font.SysFont(None, 34)
        optionsTextSurface = font.render("[N]ew game      [L]oad game      [Q]uit", True, (255, 255, 255))
        optionsTextSurfaceRect = optionsTextSurface.get_rect()
        # textRect.center = (self.screenWidth // 2, self.screenHeight // 2)
        contentBlock.blit(
            optionsTextSurface,
            (self.screenWidth // 2 - optionsTextSurfaceRect.width / 2, self.screenHeight // 2 + gameOverTextSurfaceRect.height + 30)
        )

        scoreBlock = self.buildPlayerIconTextBlock(tick, self.trophyIconImage, str(scene.player.score))
        extinguishedFiresBlock = self.buildPlayerIconTextBlock(tick, self.extinguishedFireIconImage,
                                                               str(scene.player.extinguishedFiresCount))
        notExtinguishedFiresBlock = self.buildPlayerIconTextBlock(tick, self.fireIconImage,
                                                                  str(scene.player.notExtinguishedFiresCount))

        elementsMaxHeight = max(
            scoreBlock.get_rect().height,
            extinguishedFiresBlock.get_rect().height,
            notExtinguishedFiresBlock.get_rect().height,
        )

        statisticsInitX = self.screenWidth // 2 - (scoreBlock.get_rect().width + extinguishedFiresBlock.get_rect().width + notExtinguishedFiresBlock.get_rect().width) / 2
        contentBlock.blit(
            scoreBlock,
            (
                statisticsInitX,
                self.screenHeight // 2 - (elementsMaxHeight + 50)
             )
        )
        contentBlock.blit(
            extinguishedFiresBlock,
            (
                statisticsInitX + scoreBlock.get_rect().width + 10,
                self.screenHeight // 2 - (elementsMaxHeight + 50)
            )
        )
        contentBlock.blit(
            notExtinguishedFiresBlock,
            (
                statisticsInitX + scoreBlock.get_rect().width + 10 + extinguishedFiresBlock.get_rect().width + 10,
                self.screenHeight // 2 - (elementsMaxHeight + 50)
            )
        )

        self.screen.blit(contentBlock, (0, 0))

        pygame.display.flip()

    def renderBlackScreen(self, text: str = None) -> None:
        self.screen.fill((0, 0, 0))

        font = pygame.font.SysFont(None, 48)
        text = font.render(text, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.screenWidth // 2, self.screenHeight // 2)

        self.screen.blit(text, textRect)
        pygame.display.flip()

    def handleEvents(self) -> None:
        for event in pygame.event.get(eventtype=pygame.QUIT):
            dispatcher.send(signal=GameQuit.NAME, sender=None, data={"event": GameQuit()})

            break

    def getPressedKeyGenerator(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_UP]: yield pygame.K_UP
        if pressedKeys[pygame.K_DOWN]: yield pygame.K_DOWN
        if pressedKeys[pygame.K_LEFT]: yield pygame.K_LEFT
        if pressedKeys[pygame.K_RIGHT]: yield pygame.K_RIGHT

        for event in pygame.event.get(eventtype=pygame.KEYDOWN):
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]: continue

            yield event.key

    def stop(self) -> None:
        pygame.quit()