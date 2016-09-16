import pygame
import os

##
# The player
##
class Player(pygame.sprite.Sprite):

    name = ""
    rect = None
    pace = 0
    display = None

    movementDirections = ["UP", "DOWN", "LEFT", "RIGHT"]

    def __init__(self, display, name, pace, position=()):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.display = display
        # TODO: make player size variable
        self.image = pygame.image.load("/home/phil/yasg/assets/player/player_model_small.png")
        self.rect = self.image.get_rect()
        self.pace = pace

    def move(self, direction):
        if direction in self.movementDirections:
            if direction == "UP":
                if self.rect.top > 0:
                    self.rect = self.rect.move(0, -self.pace)
            elif direction == "DOWN":
                if self.rect.bottom < self.display.get_height():
                    self.rect = self.rect.move(0, self.pace)
            elif direction == "RIGHT":
                if self.rect.right < self.display.get_width():
                    self.rect = self.rect.move(self.pace, 0)
            elif direction == "LEFT":
                if self.rect.left > 0:
                    self.rect = self.rect.move(-self.pace, 0)

    def set_pace(self, pace):
        self.pace = pace
