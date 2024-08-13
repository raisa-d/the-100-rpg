# The 100 Role Player Game
<img src="/The100RPG.gif" alt="gif playing through parts of the 100 RPG">

**The 100 RPG** is a text-based role-playing game set in the world of "The 100," inspired by the TV show. In this game, you can create characters, embark on adventures, explore the post-apocalyptic world, and engage in battles. **I am currently cleaning this code in another repository. If you want to see the current progress on the more organized version of what I have so far, click [here](https://github.com/raisa-d/RPGClean).

## Table of Contents
- [About](#the-100-role-player-game)
- [Development Status](#development-status)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Optimizations](#optimizations)
- [Lessons Learned](#lessons-learned)
- [How to Play](#how-to-play)
- [Bugs](#bugs)
- [Inspiration](#inspiration)

## Development Status

As of 1/19/2024, the game is in the early stages of development. Key functionalities such as the effects of Tek and other items are being fleshed out & implemented. In-game items and storyline flowchart are also in early stages of development. Code sections marked with "###" indicate areas that are still under construction. 
**I am currently working on re-doing the code in a bit of a more modular/best practice way. You can see that [here](https://github.com/raisa-d/RPGClean)**

NOTE: main.py is always published with extensive notes regarding what has changed since the last github update, bugs, next steps, and ideas to build on. 
Please look at those notes if you want to see more of an in-depth play-by-play of game progress!

## Installation

To get started, follow these steps:

1. Clone this repository to your local machine.
2. Install Python 3 along with the required libraries: `random`, `os`, `pickle`, and `time`.

## Usage

- Choose your character's crime that suits your playstyle.
- Explore the world of "The 100."
- Engage in thrilling turn-based battles with various enemies.
- Manage your inventory and collect items.
- Have unique interactions with NPCs based on your player's crime.

## Features

- Robust inventory management system for items and weapons.
- Save and load game progress to continue your journey.
- Engaging turn-based combat system that tests your skills.

## Optimizations
1) Cleaner code -- I am in the process of basically redoing what I have so far in a cleaner way that adheres better to best practice when using Object-Oriented Programming principles. That repository is [here](https://github.com/raisa-d/RPGClean). This project is the first big coding project I ever started, so it has been a lot of trial and error and I end up coming back to it after my skills have levelled up and wanting to completely change the back end!
2) Using Flask or Django to bring this game online so it is more widely accessible.
3) I have considered redoing the whole thing in JavaScript and getting it online that way and designing a front end, since the game currently exists on the command line.

## Lessons Learned
Since this is the first big coding project I ever started, I have learned a LOT building this role-player game. 
One of the biggest things I learned to make this game was Object-Oriented Programming. At first, when I was figuring out how I would create the player, characters, and objects/items, I tried to use dictionaries and arrays to store that data. The more research I did and other RPGs I looked at, the more I recognized others were using this magical OOP. I figured out how it worked and started using it immediately and boy did it save me soooo many lines of code.
In building this game, I have had countless bugs come up and features not work right, which really helped me think like an engineer by having to constantly think of multiple solutions to problems and try them out until one inevitably worked.

## How to Play

1. Launch the game.
2. Select a character crime to begin your adventure.
3. Navigate through the game world by typing commands.
4. Participate in battles by entering attack commands.
5. Manage your inventory using specific commands.

## Bugs

1. In the minigame to fix the dropship propulsion system, sometimes it will still ask user for input after they already solved the code completely. In this case, it requires user to click enter before it will say it is correct.
2. In the trial fight with Dante, the game may crash if you win the battle.

The game developer is working to resolve these issues.

## Inspiration

The creation of this game was inspired by the CW's "The 100" and other text-based Python RPGs, such as "Farcore" by OverdriveReplit. You can check it out [here](https://replit.com/@OverdriveReplit/Farcore?v=1#main.py).

Feel free to explore, contribute, or provide feedback to help improve "The 100 Role Player Game." Enjoy your adventure in the world of "The 100"!
