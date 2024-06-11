from __future__ import annotations  # enables forward declaratoin for type hints
import pygame.font

# ^ lts pygame render text to the screen
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    def __init__(self, ai_game: AlienInvasion, msg) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width, self.height = (200, 50)
        self.button_color = (0, 255, 0)

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # None=default font, 48=font size

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendeed image and center text on screen"""
        #                                               background color--vv
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # ^^ creates a surface for the text/message
        # "True" turns on antialiasing which makes the edges of the text smoother
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        # draw the button onto the screen. fills the necessary rectangle on screen
        self.screen.blit(self.msg_image, self.msg_image_rect)
