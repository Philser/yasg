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
            self.worldSprites = self.world.getSprites()
            self.worldMap = self.world.getWorld()

    def generateBlocklist(self):
        blockSprite = self.worldSprites[self.world.BLOCK]
        blocklist = pygame.sprite.OrderedUpdates()

        # TODO:
        # TODO: get rid of hardcoded block width and height
        for column in range(0, len(self.worldMap)):
            for line in range(0, len(self.worldMap[column])):
                if self.worldMap[column][line] == self.world.BLOCK:
                    print "Found a Block!"
                    # Test
                    newBlock = pygame.sprite.Sprite()
                    newBlock.image = blockSprite.image
                    newBlock.rect = newBlock.image.get_rect()
                    newBlock.rect.top = column * 20 + 1
                    newBlock.rect.left = line * 12 + 1
                    blocklist.add(newBlock)

        return blocklist

    def generatePlayer(self):
        newPlayer = self.worldSprites[self.world.PLAYER]
        for columns in range(0, len(self.worldMap)):
            for lines in range(0, len(self.worldMap[columns])):
                if lines == self.world.PLAYER:
                    newPlayer.rect.left = lines * 12  # +1 for better optics. ADD BORDER TO SPRITE!
                    newPlayer.rect.top = columns * 10

        return newPlayer