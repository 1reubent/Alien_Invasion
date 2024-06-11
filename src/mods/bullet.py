from __future__ import annotations  # enables forward declaratoin for type hints
import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING
# import TYPE_CHECKING constant, which allows for conditional imports that only execute for type checking, not at runtime

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    # prevents alieninvasion from being imported at runtime. only for type checking in VS code


# a sprites are game elements that can be grouped together
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game: AlienInvasion) -> None:
        """create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        # bullet is not based on an image, so we create it from scratch using Rect()
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )

        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullets position in an attribute
        self.y = float(self.rect.y) # don't need x coordinate
        # as a float so we can increment/decrement finely

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        #                ^on what surface         ^ where & how big
        