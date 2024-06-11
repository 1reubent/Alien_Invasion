# Alien Invasion - README

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Gameplay](#gameplay)
- [Controls](#controls)
- [Project Structure](#project-structure)
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
1. Clone the Repository:
   ```bash
   git clone https://github.com/1reubent/alien_invasion.git
   cd alien_invasion_game
   


2. Install Pygame:
    ```bash
    pip install pygame

3. Run the Game:
    ```bash
    python alien_invasion.py

## Gameplay
In Alien Invasion, your objective is to shoot down all the alien invaders before they reach the bottom of the screen or hit the ship. As you progress through the levels, the aliens will move faster, and the game will become more challenging.

## Controls
- Return or Click play button: start game
- Left anad right Arrow Keys: Move the spaceship left and right.
- Spacebar: Shoot bullets.
- P Key: Pause the game.
- Q Key: Quit the game.

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

- alien_invasion.py: The main module to run the game.
- alien.py: Defines the alien class.
- bullet.py: Defines the bullet class.
- button.py: Defines the button class for game interaction.
- game_stats.py: Tracks game statistics.
- scoreboard.py: Manages the scoring system.
- settings.py: Contains all the game settings.
- ship.py: Defines the rocketship class.

## Credits
Alien Invasion was developed by Reuben Thomas. The game was inspired by the classic Space Invaders arcade game. Special thanks to the contributors of the Pygame library for making game development in Python accessible and fun.

Enjoy defending Earth from the alien invasion!