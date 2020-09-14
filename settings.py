class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise the game's settings"""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_colour = (10,0,25)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255,255,255)
        self.bullets_allowed = 3

        # Star settings
        self.density = 1.0

        # Alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 is left
        self.fleet_direction = 1