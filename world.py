import pygame
import player


##
# Class that generates the game world
##

# For now it generates the world on a random basis
class World:
    def __init__(self, worldName):
        self.worldName = worldName
        self.world = None

        if worldName == "world001":
            import world001
            self.world = world001.World()
            self.worldImages = self.world.getImages()
            self.worldMap = self.world.getWorld()

    def generateObstacleList(self):
        blockImage = self.worldImages[self.world.BLOCK]
        pelletImage = self.worldImages[self.world.PELLET]
        obstaclelist = pygame.sprite.OrderedUpdates()

        # TODO: get rid of hardcoded block width and height
        for line in range(0, len(self.worldMap)):
            for column in range(0, len(self.worldMap[line])):
                if self.worldMap[line][column] == self.world.BLOCK:
                    newBlock = pygame.sprite.Sprite()
                    newBlock.type = 'BLOCK'
                    newBlock.image = blockImage
                    newBlock.rect = newBlock.image.get_rect()
                    newBlock.rect.top = line * 50  # 50 = height of block
                    newBlock.rect.left = column * 50  # 50 = width of block
                    obstaclelist.add(newBlock)
                elif self.worldMap[line][column] == self.world.PELLET:
                    newPellet = pygame.sprite.Sprite()
                    newPellet.type = 'PELLET'
                    newPellet.image = pelletImage
                    newPellet.rect = newPellet.image.get_rect()
                    newPellet.rect.top = line * 50  # 50 = height of block
                    newPellet.rect.left = column * 50 + 25 # 50 = width of block
                    obstaclelist.add(newPellet)

        return obstaclelist

    def generatePlayer(self):
        newPlayer = player.Player(2, self.worldImages[self.world.PLAYER])
        for line in range(0, len(self.worldMap)):
            for column in range(0, len(self.worldMap[line])):
                if self.worldMap[line][column] == self.world.PLAYER:
                    newPlayer.rect.left = column * 50
                    newPlayer.rect.top = line * 50

        return newPlayer

    def generatePelletList(self):
        pelletImage = self.worldImages[self.world.PELLET]
        pelletList = pygame.sprite.OrderedUpdates()

        # TODO: get rid of hardcoded block width and height
        for line in range(0, len(self.worldMap)):
            for column in range(0, len(self.worldMap[line])):
                if self.worldMap[line][column] == self.world.PELLET:
                    newPellet = pygame.sprite.Sprite()
                    newPellet.type = 'PELLET'
                    newPellet.image = pelletImage
                    newPellet.rect = newPellet.image.get_rect()
                    newPellet.rect.top = line * 50  # 50 = height of block
                    newPellet.rect.left = column * 50 + 25 # 50 = width of block
                    pelletList.add(newPellet)

        return pelletList
