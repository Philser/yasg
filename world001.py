import pygame
import player


# TODO: WHAT THE FUCK IS A SPRITE; ACTUALLY?
class World:
    def __init__(self):
        self.BLOCK = 0
        self.PLAYER = 1
        self.PELLET = 2

    def getWorld(self):
        world = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 9, 9, 9, 9, 9, 9, 9, 0],
                 [0, 2, 0, 0, 0, 9, 0, 0, 9, 0],
                 [0, 2, 0, 9, 9, 9, 9, 0, 9, 0],
                 [0, 1, 9, 9, 9, 9, 9, 0, 9, 0],
                 [0, 2, 0, 9, 9, 9, 9, 9, 9, 0],
                 [0, 2, 0, 9, 9, 9, 9, 0, 9, 0],
                 [0, 2, 0, 0, 0, 0, 0, 0, 9, 0],
                 [0, 2, 9, 9, 9, 9, 9, 9, 9, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        return world

    def getImages(self):
        playerImage = pygame.image.load("assets/player/player_model_small.png")
        blockImage = pygame.image.load("assets/world/block_large.png")
        pelletImage = pygame.image.load("assets/world/pellet.png")


        return [blockImage, playerImage, pelletImage]
