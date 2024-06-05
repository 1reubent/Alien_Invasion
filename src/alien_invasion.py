import pygame
import sys

# ^used to exit the game when we're finished

from mods.ship import Ship

# class that holds the ship information
from mods.settings import Settings
# class that holds game settings

from mods.bullet import Bullet

FULLSCREEN = True


class AlienInvasion:
    """Class to manage the game assets and behavior"""

    def __init__(self) -> None:
        """init game"""
        pygame.init()
        # ^ inits background settings
        self.settings = Settings()
        # this class contains all the default settings for initing the game
        if FULLSCREEN:
            # basically tell pygame to find a screen size that fills the entire screen
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            # set the settings attributes to the appropriate values
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )

        # creates a display window; specify dimensions as a tuple. assigns it as an attribute
        # returns  a 'surface' or a part of the screen where a game element can be displayed.
        # every element is its own surface
        pygame.display.set_caption("Alien Invasion")
        # name of the game (window name)

        # # Set background color
        # self.bg_color = (230, 230, 230)
        #     # RGB tuple
        # create a ship
        self.ship = Ship(self)

        # create a sprite group of bullets
        # hold all the currently fired bullets in a sprite group
        self.bullets = pygame.sprite.Group()  # type: pygame.sprite.Group

    def run_game(self):
        """Start the main loop for the game"""
        # main event loop:
        while True:
            self._check_events()  # update the game based on any new user inputs
            self.ship.update()  # update ship position based on any flag updates from _check_events()
            self._update_bullets()
            self._update_screen()  # update the screen with the new changes

    def _update_bullets(self):
        # update existing bullet positions
        self.bullets.update()  # update bullets' positions. Group automatically calls update() for every bullet (sprite) in the group

        # remove unnecessary bullets:
        # create a copy so that we can remove from the group as we iterate through it
        current_bullets: list[Bullet] = self.bullets.copy()  # type: ignore
        for bullet in current_bullets:
            # if bullet is off the top of the screen (its bottom is at y=0), remove it from the group
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        # a single leading underscore indicates a helper method in a class.
        # helper methods are not meant to be directly called
        """respond to keypresses and mouse movements"""

        for event in pygame.event.get():  # << this function returns a list of events since the last time it was called
            # an 'event' is an action the user performs while playing the game (kb and mouse inputs)
            # this "event loop" listens for events and performs appropriate tasks

            # QUIT EVENT
            if event.type == pygame.QUIT:
                sys.exit()
                # this exits the game if the user presses the windows close button

            # KEYDOWN EVENT
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # KEYUP EVENTS
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            # set the moving right flag so that in run_game(), the ship will be continuously moved right
        elif event.key == pygame.K_LEFT:
            # can use 'elif' because each key press is an independent event
            self.ship.moving_left = True

        # check if user fired a bullet
        elif event.key == pygame.K_SPACE:
            # can use 'elif' because each key press is an independent event
            self._fire_bullet()

        # check if user quit
        elif event.key == pygame.K_q:
            # quit if 'q' is pressed
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            # reset the moving_right flag, so that it stops moving right
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """update screen color, ship location, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        # on each loop set the color of a surface by useing the .fill(color) method
        # specificy color as an RGB tuple

        # set the ship in its place
        self.ship.blitme()

        # manually draw each bullet in the group attribute
        # returns a list of bullets
        current_bullets: list[Bullet] = self.bullets.sprites()  # type: ignore
        for bullet in current_bullets:
            bullet.draw_bullet()

        # this function just updates the screen on every run of the while loop, so any updates to game elements are shown
        pygame.display.flip()

    def _fire_bullet(self):
        # Create new bullet, and add it to the group attribute IF the currently existing bullets is < # allowed
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
