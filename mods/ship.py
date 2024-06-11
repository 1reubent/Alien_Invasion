from __future__ import annotations  # enables forward declaratoin for type hints
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
# import TYPE_CHECKING constant, which allows for conditional imports that only execute for type checking, not at runtime

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    # prevents alieninvasion from being imported at runtime. only for type checking in VS code


class Ship(Sprite):
    """class to manage the ship in Alien invasion"""

    def __init__(self, ai_game: AlienInvasion) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # everything in pygame is a 'rectangle'.
        # use the rectangle attribute of a surface to manipulate it easily
        # this makes the game resources an attribute of the ship, allowing them to be accessed in following methods

        self.screen_rect = ai_game.screen.get_rect()
        # doing this allows you to place the ship in the right place on the screen

        self.image = pygame.image.load(
            "images/rocket.bmp",
        )
        # returns a surface representing the ship
        ship_size = (self.image.get_width() // 16, self.image.get_height() // 16)
        self.image = pygame.transform.scale(self.image, ship_size)
        self.rect = self.image.get_rect()
        # returns the surface as a rectangle

        # set the ship at the middle-bottom of the screen, by setting the ship's midbottom to the screen's
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        # rect can only hold integer values. To appropriately update the ships position we need a float
        # rect.x is the x coordinate of the ships top left corner
        self.y = float(self.rect.y)

        # These are the movement flags to help enable continuous movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):  # draw the ship to the screen
        self.screen.blit(self.image, self.rect)
        # blit() draws a surface to the screen. it takes the surface and it's rect

    def update(self):
        """update ship position"""
        # update ship position based on ship speed. Update the 'x' attribute not 'rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # check to make sure the right of the ship is not passed the screen
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            # if its elif, then you cant press < and > at the same time
            # check to make sure the left of the ship is not passed the screen
            self.x -= self.settings.ship_speed

        # Update rect with new value. It will be rounded but thats ok
        self.rect.x = self.x

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
            
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
