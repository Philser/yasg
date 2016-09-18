import pygame

##
# A simple block that exists to block the player
##
class WorldBlock(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("/home/phil/PycharmProjects/yasg/assets/world/block.png")
		self.rect = self.image.get_rect()
