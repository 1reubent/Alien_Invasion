"""simple rocket moving pygame app"""

import sys
import pygame


class RocketGame:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rocket = Rocket(self)

        pygame.display.set_caption("Rocket Game")

    def run_game(self):
        while True:
            self._check_update()
            self.rocket.update()
            self._update_screen()

    def _check_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rocket.moving_down = False

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.rocket.blitme()
        pygame.display.flip()


class Rocket:
    def __init__(self, game: RocketGame) -> None:
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # doing this allows you to place the ship in the right place on the screen

        self.image = pygame.image.load(
            "rocket.bmp",
        )
        ship_size = (self.image.get_width() // 16, self.image.get_height() // 16)
        self.image = pygame.transform.scale(self.image, ship_size)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1

    # draws rocket to the screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # blit() draws a surface to the screen. it takes the surface and it's rect


if __name__ == "__main__":
    rocket_game = RocketGame()
    rocket_game.run_game()
