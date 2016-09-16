import pygame
import world_block
import random

##
# Class that generates the game world
##

# For now it generates the world on a random basis
# TODO: Generate by means of a plan
class World:
	blocklist = None

	def __init__(self):
		pass

	def generate(self, display):
		self.blocklist = pygame.sprite.OrderedUpdates()
		
		for i in range(1, 11):
			block = world_block.WorldBlock()
			# TODO: add random value calculation in bounds of display
			rand_x = random.randrange(0, display.get_width())
			rand_y = random.randrange(0, display.get_height())
			block.rect.left = rand_x
			block.rect.top = rand_y
			self.blocklist.add(block)

		return self.blocklist

	def getObjectForTopLeftPos(self, x, y):
		for block in self.blocklist:
			if block.rect.left == x and block.rect.top == y:
				return block
			else:
				return None
		
