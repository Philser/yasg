import pygame
import player
import eventHandler
import world


# TODO: Change filenames to be Capitalcase
class App:
    gameRunning = False
    DISPLAY = None
    player = None
    background = None
    clock = None
    eventHandler = None
    updatedSprites = None

    # TODO: keep a list of sprites that have to be drawn every time smth is updated (like world and background)
    # TODO: Make world use whole display
    # TODO: Draw blocks on background once and then save that image for reuse instead of drawing each block again each time
    # TODO: keep one list holding both blocks and pellets
    # TODO: Add bad guys
    # TODO: Strategy pattern for their different behaviours
    def __init__(self, screen_x, screen_y):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode((screen_x, screen_y))

        # init background
        self.background = pygame.Surface(self.DISPLAY.get_size())
        self.background.convert()
        self.background.fill(pygame.Color("white"))

        self.updatedSprites = pygame.sprite.OrderedUpdates()

        # init world
        # TODO: Get rid of "worldBlocks"
        self.world = world.World("world001")
        self.worldBlocks = self.world.generateObstacleList()
        self.updatedSprites.add(self.worldBlocks)

        self.worldPellets = self.world.generatePelletList()
        self.updatedSprites.add(self.worldPellets)
        # init player
        self.player = self.world.generatePlayer()

        self.updatedSprites.add(self.player)

        # init event handler
        self.eventHandler = eventHandler.EventHandler(self.player, self.world, self.worldBlocks, self.worldPellets, self.DISPLAY)

        self.clock = pygame.time.Clock()

        # initial drawing
        self.DISPLAY.blit(self.background, (0, 0))
        self.updatedSprites.draw(self.DISPLAY)

        self.gameRunning = True

    def main(self):
        while self.gameRunning:
            self.clock.tick(60)
            pygame.display.flip()

            self.updatedSprites = self.eventHandler.handle_events(pygame.event.get(), pygame.key.get_pressed())
            self.gameRunning = not self.eventHandler.received_quit_event()

            if self.updatedSprites:
                self.updatedSprites.add(self.worldBlocks)
                self.updatedSprites.add(self.worldPellets)
                self.DISPLAY.blit(self.background, (0, 0))
                self.updatedSprites.draw(self.DISPLAY)


app = App(500, 500)
app.main()
