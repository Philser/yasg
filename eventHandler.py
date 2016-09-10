import pygame
from pygame import locals


class EventHandler:

    player = None

    def __init__(self, player):
        self.player = player
        pass

    # TODO: handle QUIT event
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
        #elif keys[pygame.K_ESCAPE]:

        for event in eventList:
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
