import pygame
import player


# TODO: WHAT THE FUCK IS A SPRITE; ACTUALLY?
class World:
    def __init__(self):
        self.BLOCK = 0
        self.PLAYER = 1

    def getWorld(self):
        world = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [9, 9, 9, 0, 0, 0, 0, 9, 9, 9],
                 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                 [1, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        return world

    def getImages(self):
        playerImage = pygame.image.load("assets/player/player_model_small.png")

        blockImage = pygame.image.load("assets/world/block.png")


        return [blockImage, playerImage]
