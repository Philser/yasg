import pygame
import os


##
# The player
##
class Player(pygame.sprite.Sprite):
    movementDirections = ["UP", "DOWN", "LEFT", "RIGHT"]

    def __init__(self, pace, image=pygame.image):
        pygame.sprite.Sprite.__init__(self)
        # TODO: make player size variable
        self.pace = pace
        self.image = image
        self.rect = self.image.get_rect()

    def move(self, direction, obstacles, display):
    	if direction in self.movementDirections:
            if direction == "UP":
                if self.rect.top > 0 and self.can_move(self.rect.left, self.rect.top - self.pace, obstacles):
                    self.rect = self.rect.move(0, -self.pace)
            elif direction == "DOWN":
                if self.rect.bottom < display.get_height() and self.can_move(self.rect.left, self.rect.top + self.pace, obstacles):
                    self.rect = self.rect.move(0, self.pace)
            elif direction == "RIGHT":
                if self.rect.right < display.get_width() and self.can_move(self.rect.left + self.pace, self.rect.top, obstacles):
                    self.rect = self.rect.move(self.pace, 0)
            elif direction == "LEFT":
                if self.rect.left > 0 and self.can_move(self.rect.left - self.pace, self.rect.top, obstacles):
                    self.rect = self.rect.move(-self.pace, 0)

    def set_pace(self, pace):
        self.pace = pace

    def can_move(self, new_x, new_y, obstacles):
        test_rect = self.rect.copy()
        test_rect.left = new_x
        test_rect.top = new_y

        for obstacle in obstacles:
        	if obstacle.type == 'PELLET':
        		obstacles.remove(obstacle)
        	elif test_rect.colliderect(obstacle.rect):
            		return False        
        return True
