import pygame
import os


##
# The abstract Class for the player's enemies
##
class Ghost(pygame.sprite.Sprite):

    movementDirections = ["UP", "DOWN", "LEFT", "RIGHT"]

    def __init__(self, pace, image=pygame.image):
        pygame.sprite.Sprite.__init__(self)
        # TODO: make player size variable
        self.pace = pace
        self.image = image
        self.rect = self.image.get_rect()

    def move(self, direction, display):
        if direction in self.movementDirections:
            if direction == "UP":
                if self.rect.top > 0:
                    self.rect = self.rect.move(0, -self.pace)
            elif direction == "DOWN":
                if self.rect.bottom < display.get_height():
                    self.rect = self.rect.move(0, self.pace)
            elif direction == "RIGHT":
                if self.rect.right < display.get_width():
                    self.rect = self.rect.move(self.pace, 0)
            elif direction == "LEFT":
                if self.rect.left > 0:
                    self.rect = self.rect.move(-self.pace, 0)

    def set_pace(self, pace):
        self.pace = pace
