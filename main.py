import pygame
import player
from pygame.locals import *


class App:

    GAME_RUNNING = False
    DISPLAY = None
    player = None
    background = None
    clock = None


    def __init__(self, screen_x, screen_y):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode((screen_x, screen_y))

        # draw background to screen
        self.background = pygame.Surface(self.DISPLAY.get_size())
        self.background.convert()
        self.background.fill((255,255,255))
        self.DISPLAY.blit(self.background, (0,0))
        pygame.display.flip()

        self.player = player.Player(self.DISPLAY, "John Doe", 10, (0,0))
        self.player.draw()

        self.clock = pygame.time.Clock()

        self.GAME_RUNNING = True

    def main(self):
        while self.GAME_RUNNING:
            self.clock.tick(60)
            pygame.display.flip()

            # TODO: Create EventHandler class
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.DISPLAY.blit(self.background, (0, 0))
                self.player.move("UP")
            elif keys[pygame.K_DOWN]:
                self.DISPLAY.blit(self.background, (0, 0))
                self.player.move("DOWN")
            elif keys[pygame.K_RIGHT]:
                self.DISPLAY.blit(self.background, (0, 0))
                self.player.move("RIGHT")
            elif keys[pygame.K_LEFT]:
                self.DISPLAY.blit(self.background, (0, 0))
                self.player.move("LEFT")


            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

app = App(800, 600)
app.main()
