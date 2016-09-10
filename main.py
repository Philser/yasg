import pygame
import player
import eventHandler


class App:

    GAME_RUNNING = False
    DISPLAY = None
    player = None
    background = None
    clock = None
    eventHandler = None

    def __init__(self, screen_x, screen_y):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode((screen_x, screen_y))

        # draw background to screen
        self.background = pygame.Surface(self.DISPLAY.get_size())
        self.background.convert()
        self.background.fill(pygame.Color("white"))
        self.DISPLAY.blit(self.background, (0,0))
        pygame.display.flip()

        # init player
        self.player = player.Player(self.DISPLAY, "John Doe", 10, (0, 0))
        self.player.draw()

        # init event handler
        self.eventHandler = eventHandler.EventHandler(self.player)

        self.clock = pygame.time.Clock()

        self.GAME_RUNNING = True

    # TODO: add background blit -- maybe via surfaceList?
    def main(self):
        while self.GAME_RUNNING:
            self.clock.tick(60)
            pygame.display.flip()

            self.eventHandler.handle_events(pygame.event.get(), pygame.key.get_pressed())


app = App(800, 600)
app.main()
