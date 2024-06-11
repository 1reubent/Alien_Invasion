# TODO: new pygame font????

import json
import pygame
import sys
from time import sleep
# ^used to exit the game when we're finished

from mods.ship import Ship
# class that holds the ship information

from mods.settings import Settings

# class that holds game settings
from mods.scoreboard import Scoreboard
from mods.game_stats import GameStats
from mods.bullet import Bullet
from mods.alien import Alien
from mods.button import Button

FULLSCREEN = True
DEBUG = True
FILENAME = "highscore.json"


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

        # get background
        self.bg = pygame.image.load("images/bg.jpg")
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_width, self.settings.screen_height)
        )
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.center = self.screen.get_rect().center
        # get background opacity rect
        self.bg_surface = pygame.Surface(
            (self.screen.get_rect().width, self.screen.get_rect().height),
            pygame.SRCALPHA,
        )
        self.bg_surface.fill((230, 230, 230, 85))

        # # Set background color
        # self.bg_color = (230, 230, 230)
        #     # RGB tuple
        # create a ship
        self.ship = Ship(self)

        # set initial game stats
        self.stats = GameStats(self)
        # set scoreboard
        self.sb = Scoreboard(self)

        # create a sprite group of bullets
        # hold all the currently fired bullets in a sprite group
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        # create initial fleet of aliens
        self._create_fleet()

        # make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""

        # main event loop:
        while True:
            self._check_events()  # update the game based on any new user inputs
            if self.stats.game_active:
                self.ship.update()  # update ship position based on any flag updates from _check_events()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()  # update the screen with the new changes

    def _check_events(self):
        # a single leading underscore indicates a helper method in a class.
        # helper methods are not meant to be directly called
        """respond to keypresses and mouse movements"""

        for event in pygame.event.get():  # << this function returns a list of events since the last time it was called
            # an 'event' is an action the user performs while playing the game (kb and mouse inputs)
            # this "event loop" listens for events and performs appropriate tasks

            # QUIT EVENT
            if event.type == pygame.QUIT:
                self._write_current_highscore()
                sys.exit()
                # this exits the game if the user presses the windows close button

            # KEYDOWN EVENT
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # KEYUP EVENTS
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.stats.game_active:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button_click(mouse_pos)
                    # returns a tuple containing the mouse cursors (x,y) when click occured

    def _check_play_button_click(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
            if not self.stats.game_paused:
                # Reset game stats, bullets, ships, and aliens
                self.settings.initialize_dynamic_settings()  # reset dynamic settings
                self.stats.reset_stats()
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_ships()

                self.aliens.empty()
                self.bullets.empty()

                self._create_fleet()
                self.ship.center_ship()
                pygame.mouse.set_visible(False)
                # make mouse cursor invisible
            self.stats.game_paused = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            # set the moving right flag so that in run_game(), the ship will be continuously moved right
        elif event.key == pygame.K_LEFT:
            # can use 'elif' because each key press is an independent event
            self.ship.moving_left = True

        # check if user fired a bullet

        elif self.stats.game_active and event.key == pygame.K_SPACE:
            # can use 'elif' because each key press is an independent event
            self._fire_bullet()

        # check if user quit
        elif event.key == pygame.K_q:
            # quit if 'q' is pressed
            self._write_current_highscore()
            sys.exit()
        elif event.key == pygame.K_RETURN:
            if not self.stats.game_active:
                mouse_pos = self.play_button.rect.center
                self._check_play_button_click(mouse_pos)
        elif event.key == pygame.K_p:
            self.stats.game_active = False
            self.stats.game_paused = True
            pygame.mouse.set_visible(True)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            # reset the moving_right flag, so that it stops moving right
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        # update existing bullet positions
        self.bullets.update()  # update bullets' positions. Group automatically calls update() for every bullet (sprite) in the group

        # remove unnecessary bullets:
        # create a copy so that we can remove from the group as we iterate through it
        current_bullets: list[Bullet] = self.bullets.copy()
        for bullet in current_bullets:
            # if bullet is off the top of the screen (its bottom is at y=0), remove it from the group
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # check for collisions with aliens
        # this checks whether any elements of either group have collided with each other
        # then it deletes both the alien and the bullet that collided (True, True)
        # it also returns a dictionary of bullets that have collided with aliens (bullet:alien)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # TODO: simulatenous collisions not registering?
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()  # creates a new image for the updated score
                self.sb.check_high_score()

        # if aliens are all gone, delete all existing bullets and create new fleet
        if not self.aliens:
            self._update_screen()  # get frame of the last hit
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()  # make game harder

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()
            sleep(1.0)  # pause on the last frame

    def _create_alien(self, alien_num, row_num):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.set_x(
            alien_width + alien_num * (2 * alien_width)
        )  # margin + alien_num*(2 * alien_width)

        alien.set_y(alien_height + row_num * (2 * alien_height))
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # create alien to use as reference to make calculatons (not added to fleet)
        alien = Alien(self)
        (alien_width, alien_height) = alien.rect.size

        # calculate the number of aliens in a row
        available_space_x = self.settings.screen_width - (
            2 * alien_width
        )  # 1 alien width margin on both sides
        num_aliens_x = available_space_x // (
            2 * alien_width  #            ^floor division or int division
        )  # 1 alien width gap between aliens

        # calculate the number of rows
        available_space_y = (
            self.settings.screen_height - 3 * alien_height - self.ship.rect.height
        )  # 1 alien_height margin at the top, ship_height + 2 * alien_height at the bottom
        num_rows = available_space_y // (2 * alien_height)
        # 1 extra alien height gap between rows
        for row_num in range(num_rows):
            for alien_num in range(num_aliens_x):
                self._create_alien(alien_num, row_num)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        self._check_ship_alien_collision()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Change fleet direction if any alien has hit an edge"""
        current_aliens: list[Alien] = self.aliens.sprites()
        for alien in current_aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        current_aliens: list[Alien] = self.aliens.sprites()
        for alien in current_aliens:
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_ship_alien_collision(self):
        # if aliens hit ship, need to reset
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        current_aliens: list[Alien] = self.aliens.sprites()
        for alien in current_aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        # on a hit, subtract ships left, remove all aliens and bullets, create new fleet and center ship
        if self.stats.ships_left > 0:
            self._update_screen()  # get last hit frame
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            if DEBUG:
                print(f"{self.stats.ships_left} ships left")
            sleep(1.0)  # pause on last hit frame
        else:
            # end game, make mouse visible
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _blit_background(self):
        # blit background image
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.bg_surface, (0, 0))

    def _update_screen(self):
        """update screen color, ship location, and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        # on each loop set the color of a surface by useing the .fill(color) method
        # specificy color as an RGB tuple

        # blit background image
        self._blit_background()

        # set the ship in its place
        self.ship.blitme()

        # manually draw each bullet in the group attribute
        # returns a list of bullets
        current_bullets: list[Bullet] = self.bullets.sprites()
        for bullet in current_bullets:
            bullet.draw_bullet()

        # draw aliens. draw() draws each element of the group at the position defined by its rect
        self.aliens.draw(self.screen)

        # draw scoreboard
        self.sb.show_score()

        # draw Play button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # this function just updates the screen on every run of the while loop, so any updates to game elements are shown
        pygame.display.flip()

    def _fire_bullet(self):
        # Create new bullet, and add it to the group attribute IF the currently existing bullets is < # allowed
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _write_current_highscore(self):
        # save current high score
        with open(FILENAME, "w") as f:
            json.dump(self.stats.high_score, f)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
