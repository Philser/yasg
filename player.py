import pygame


class Player():
	# # # # # # # # # # # # # #
	# Player class
	# # # # # # # # # # # # # #
	
    name = ""
    appearance = None
    pace = 0
    display = None

    movementDirections = ["UP", "DOWN", "LEFT", "RIGHT"]

    def __init__(self, display, name, pace, position=()):
        self.name = name
        self.display = display
        # TODO: make player size variable
        self.appearance = pygame.Rect(position, (20, 30))
        self.pace = pace

    def draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.appearance)

    def move(self, direction):
        if direction in self.movementDirections:
            if direction == "UP":
                if self.appearance.top > 0:
                    self.appearance = self.appearance.move(0, -self.pace)
            elif direction == "DOWN":
                if self.appearance.bottom < self.display.get_height():
                    self.appearance = self.appearance.move(0, self.pace)
            elif direction == "RIGHT":
                if self.appearance.right < self.display.get_width():
                    self.appearance = self.appearance.move(self.pace, 0)
            elif direction == "LEFT":
                if self.appearance.left > 0:
                    self.appearance = self.appearance.move(-self.pace, 0)

        self.draw()

    def set_pace(self, pace):
        self.pace = pace
