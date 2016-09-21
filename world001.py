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

    def getSprites(self):
        playerSprite = player.Player(2)
        playerSprite.image = pygame.image.load("assets/player/player_model_small.png")
        playerSprite.rect = playerSprite.image.get_rect()
        blockSprite = pygame.sprite.Sprite()
        blockSprite.image = pygame.image.load("assets/world/block.png")
        blockSprite.rect = blockSprite.image.get_rect()

        return [blockSprite, playerSprite]
