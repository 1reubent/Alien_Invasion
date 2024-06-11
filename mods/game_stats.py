from __future__ import annotations  # enables forward declaratoin for type hints
import json

from typing import TYPE_CHECKING
# import TYPE_CHECKING constant, which allows for conditional imports that only execute for type checking, not at runtime

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion 

FILENAME = "highscore.json"


class GameStats:
    def __init__(self, ai_game: AlienInvasion) -> None:
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.game_paused = False
        
        # High score should not be reset
        # get and set last high score
        try:
            with open(FILENAME) as f:
                high_score = json.load(f)
                self.high_score = high_score
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
