# Hangman Game

## Project Overview

Hangman is a modular Python-based word guessing game. The player tries to guess a randomly selected word one letter at a time while having a limited number of lives.

The project demonstrates the use of Python programming concepts such as modules, functions, return statements, lists, loops, classes, and user input.

## Features

- Randomly selects a word from a word list.
- Allows the player to guess one letter at a time.
- Displays the progress of the word after each guess.
- Tracks the player's lives.
- Tracks guessed letters.
- Displays Hangman stages based on remaining lives.
- Calculates the player's score.
- Detects repeated and invalid guesses.
- Displays separate win and loss messages.

## File Description
main.py – Controls the overall game flow.
hangman_art.py – Contains the Hangman stages and game logo.
hangman_words.py – Contains the list of words used in the game.
game_logic.py – Contains functions for creating and updating the word display and checking guesses.
player.py – Contains the Player class for managing player information, lives, score, and guessed letters.
## Technologies Used
Python
Git
GitHub
Visual Studio Code
## How to Run
Clone or download the project.
Open the project folder in Visual Studio Code.
Open the terminal.
Run:
python main.py
Enter your name and start guessing letters.
Testing
The game was tested by:
Entering correct guesses.
Entering incorrect guesses.
Entering repeated guesses.
Entering invalid inputs such as numbers or multiple characters.
Checking the win condition.
Checking the loss condition.
Checking that lives and score update correctly.
## Learning Outcomes
This project demonstrates the practical use of:
Functions using def
Returning values using return
Python modules and imports
Lists
Loops
Classes and objects
Conditional statements
User input and output
Basic input validation
Future Enhancements
Add multiple difficulty levels.
Add categories of words.
Add a high-score system.
Add a graphical user interface.
Add more player statistics


## Project Structure

```text
Hangman/
│
├── main.py
├── hangman_art.py
├── hangman_words.py
├── game_logic.py
├── player.py
└── README.md 
