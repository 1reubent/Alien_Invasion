class Settings:
    """a class to store settings for Alien invasion"""

    def __init__(self) -> None:
        """init static game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # static Ship settings
        self.ship_limit = 3

        # static Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15

        # static Alien settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = (
            3.5  # we can more easily mess witht the ship speed if it's an attribute
        )
        self.bullet_speed = 5.0
        self.alien_speed = 2.0
        self.fleet_direction = 1
        # 1 = right; -1 = left
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
