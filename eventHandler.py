import pygame
from pygame import locals


class EventHandler:

    player = None
    receivedQuitEvent = False

    def __init__(self, player):
        self.player = player
        pass

    def handle_events(self, eventList, keys):

        # Player movement
        if keys[pygame.K_UP]:
            self.player.move("UP")
        elif keys[pygame.K_DOWN]:
            self.player.move("DOWN")
        elif keys[pygame.K_RIGHT]:
            self.player.move("RIGHT")
        elif keys[pygame.K_LEFT]:
            self.player.move("LEFT")
        elif keys[pygame.K_ESCAPE]:
            self.receivedQuitEvent = True

        for event in eventList:
            if event.type == pygame.QUIT:
                self.receivedQuitEvent = True

    def received_quit_event(self):
        return self.receivedQuitEvent