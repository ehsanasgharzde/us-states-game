# U.S. States Game

Welcome to the U.S. States Game! This educational and fun game is implemented in Python using the Tkinter and Pandas libraries. The game challenges players to guess and identify the U.S. states by their names and locations on a map.

## Game Overview

The U.S. States Game features an interactive map of the United States with state names. Players are presented with a blank map and are tasked with guessing the names of the U.S. states. As they correctly identify states, the game displays the state names on the map, helping players learn and remember the geography of the United States.

## Game Components

The project includes the following files and components:

- `main.py`: The main script that runs the game, manages user interactions, and displays the game window.

- `writer.py`: A custom module that handles the writing of text on the game screen, specifically displaying state names.

- `states.csv`: A CSV file containing data about U.S. states, including their names and coordinates for positioning on the map.

- `StatesYouShouldLearn.csv`: A CSV file used to save the states that the player has yet to correctly identify.

## How to Play

1. Run `main.py` to start the game.

2. A blank map of the United States is displayed.

3. Enter the names of U.S. states, and if correct, the game will display the state names on the map.

4. Keep guessing and identifying states until you have correctly identified all 50 U.S. states or choose to exit.

5. The game keeps track of your progress and displays the number of states correctly identified.

6. To exit the game, simply type 'Exit.'

7. If you exit the game, the remaining unguessed states are saved in 'StatesYouShouldLearn.csv' for future reference.

## Requirements

- Python 3.x
- Tkinter (included in most Python installations)
- Pandas library (install using `pip install pandas`)

## Installation

1. Clone the repository to your local machine.

2. Ensure you have Python 3.x and the Pandas library installed.

3. Run `main.py` to start the game.



Enjoy the game and have fun exploring the U.S. states!

