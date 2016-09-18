import pygame
from pygame import locals


##
# Center of event handling
##
class EventHandler:
    player = None
    receivedQuitEvent = False
    updatedSprites = ()

    def __init__(self, player, world):
        self.player = player
        self.world = world
        self.updatedSprites = pygame.sprite.OrderedUpdates()

    def handle_events(self, eventList, keys):
        self.updatedSprites.empty()

        # Player movement
        # TODO: improve collision detection for world objects (LEFT and UP)
        playerUpdated = True
        if keys[pygame.K_UP]:
            if self.can_move_player(self.player.rect.left, self.player.rect.top - self.player.pace):
                self.player.move("UP", self.display)
        elif keys[pygame.K_DOWN]:
            if self.can_move_player(self.player.rect.left, self.player.rect.top + self.player.pace):
                self.player.move("DOWN")
        elif keys[pygame.K_RIGHT]:
            if self.can_move_player(self.player.rect.left + self.player.pace, self.player.rect.top):
                self.player.move("RIGHT")
        elif keys[pygame.K_LEFT]:
            if self.can_move_player(self.player.rect.left - self.player.pace, self.player.rect.top):
                self.player.move("LEFT")
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

    def can_move_player(self, new_x, new_y):
        test_rect = self.player.rect.copy()
        test_rect.left = new_x
        test_rect.top = new_y

        for block in self.world.blocklist:
            if test_rect.colliderect(block.rect):
                return False
        return True
