import pygame
from pygame import locals


##
# Center of event handling
##
class EventHandler:
    player = None
    receivedQuitEvent = False
    updatedSprites = ()

    def __init__(self, player, world, blockList, pelletList, display):
        self.player = player
        self.world = world
        self.updatedSprites = pygame.sprite.OrderedUpdates()
        self.blockList = blockList
        self.pelletList = pelletList
        self.display = display

    def handle_events(self, eventList, keys):
        self.updatedSprites.empty()

        # Player movement
        # TODO: improve collision detection for world objects (LEFT and UP)
        playerUpdated = True
        if keys[pygame.K_UP]:
            self.player.move("UP", self.blockList, self.display)
        elif keys[pygame.K_DOWN]:
            self.player.move("DOWN", self.blockList, self.display)
        elif keys[pygame.K_RIGHT]:
            self.player.move("RIGHT", self.blockList, self.display)
        elif keys[pygame.K_LEFT]:
            self.player.move("LEFT", self.blockList, self.display)
        else:
            playerUpdated = False

        for event in eventList:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.receivedQuitEvent = True

        if playerUpdated:
            self.updatedSprites.add(self.player)

        return self.updatedSprites

    def received_quit_event(self):
        return self.receivedQuitEvent