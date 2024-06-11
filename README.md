# Alien Invasion - README

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Gameplay](#gameplay)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Modifying Game Settings](#modifying-game-settings)
    - [Optimization](#optimization)
    - [Fullscreen or Windowed](#fullscreen-or-windowed)
    - [Resetting High Score](#resetting-high-score)
- [Credits](#credits)

## Introduction
Alien Invasion is a classic arcade-style game inspired by the Space Invaders. The player controls a spaceship and must defend Earth from waves of descending aliens. The game is written in Python using the Pygame library, offering an exciting retro gaming experience.

## Features
- Classic Space Invaders gameplay
- Multiple levels of increasing difficulty
- Score tracking
- Simple and intuitive controls

## Requirements
- Python 3.6 or higher
- Pygame library, version 2.5.2
- ```dependencies.txt```

## Installation
1. __Clone the Repository:__
   ```bash
   git clone https://github.com/1reubent/alien_invasion.git
   cd alien_invasion
   


2. __Install Pygame:__
    ```bash
    pip install pygame

3. __Run the Game:__
    ```bash
    python alien_invasion.py

## Gameplay
In Alien Invasion, your objective is to shoot down all the alien invaders before they reach the bottom of the screen or hit the ship. As you progress through the levels, the aliens will move faster, and the game will become more challenging.

## Controls
- __Return__ or __Click play button:__ Start the game.
- __Arrow Keys:__ Move the spaceship left and right.
- __Spacebar:__ Shoot bullets.
- __P Key:__ Pause the game.
- __Q Key:__ Quit the game.

## Project Structure
```
alien_invasion_game/
│
├── images/
│   ├── alien.png
│   ├── bg.jpg
│   └── ...
│
├── mods/
│   ├── alien.py
│   ├── bullet.py
│   ├── button.py
│   ├── game_stats.py
│   ├── scoreboard.py
│   ├── settings.py
│   └── ship.py
│
├── alien_invasion.py
├── dependencies.txt
└── README.md
```
- __alien_invasion.py:__ The main module to run the game.
- __alien.py:__ Defines the alien class.
- __bullet.py:__ Defines the bullet class.
- __button.py:__ Defines the button class for game interaction.
- __game_stats.py:__ Tracks game statistics.
- __scoreboard.py:__ Manages the scoring system.
- __settings.py:__ Contains all the game settings.
- __ship.py:__ Defines the rocketship class.

## Modifying Game Settings

### Optimization
If the game runs to fast/slow, or if you just want to mess with the settings, navigate to the `settings.py` file where you can modify severl settings. Some key settings include:
- __Ship Speed:__ Controls how fast the player's ship moves.

    `self.ship_speed = 1.5`

- __Bullet Speed:__ Controls the speed of the bullets fired by the player's ship.

    `self.bullet_speed = 3.0`

- __Alien Speed:__ Controls how fast the aliens move horizontally.

    `self.alien_speed = 1.0`
- __Fleet Drop Speed:__ Controls how fast the fleet of aliens drops down the screen.

    `self.fleet_drop_speed = 10`
- __Speedup Scale:__ Controls how much the game speeds up after each level.

    `self.speedup_scale = 1.1`

- __Score Scale:__ Controls how much the score increases after each level.

    `self.score_scale = 1.5`

### Fullscreen or Windowed
You can also change whether the game runs in fullscreen or windowed mode by navigating to `alien_invasion.py` and modifying the `FULLSCREEN` macro near the top to either `True` or `False`.

### Resetting High Score
To reset the highscore, just delete `highscore.json` that should be created in `alien_invasion/` after you play the game for the first time.

## Credits
Alien Invasion was developed by Reuben Thomas. The game was inspired by the classic Space Invaders arcade game. Special thanks to the contributors of the Pygame library for making game development in Python accessible and fun.

Enjoy defending Earth from the alien invasion!


