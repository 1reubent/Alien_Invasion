from __future__ import annotations  # enables forward declaratoin for type hints
import pygame
from pygame.sprite import Sprite

# for typechecking
from typing import TYPE_CHECKING

# import TYPE_CHECKING constant, which allows for conditional imports that only execute for type checking, not at runtime

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion 
    # prevents alieninvasion from being imported at runtime. only for type checking in VS code


class Alien(Sprite):
    def __init__(self, ai_game: AlienInvasion) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # set image
        self.image = pygame.image.load("images/alien.png")
        # resize image
        # alien_size = (self.image.get_width() // 16, self.image.get_height() // 16)
        # self.image = pygame.transform.scale(self.image, alien_size)
        # get rect
        self.rect = self.image.get_rect()

        # set position (near top left corner)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store exact horizontal position
        self.x = float(self.rect.x)

    def set_x(self, num):
        self.x = num
        self.rect.x = self.x

    def set_y(self, num):
        self.rect.y = num

    def check_edges(self):
        """Return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """Move alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
