# Tic-Tac-Toe
Code for basic Tic-Tac-Toe game in python

A tic-tac-toe class that plays a game with two opponents. The point of
using a class here is to be able to use variables like the current board state
or whether or not the game is still being played easily, wherever you are in the game.

NOTE:
Run your code by making an "instance" of the class and calling the function that
starts the game.

IMPORTANT TODOs:
- Create an introductory message for the players when starting the game.
- Create the tic-tac-toe board that you can fill in as you play the game.
    - The user will play by entering the space they want their piece to be placed.
    
    - Sample Board and space number:
    
         1 | 2 | 3
        -----------
         4 | 5 | 6
        -----------
         7 | 8 | 9
         
- Set whether Player 1 or Player 2 will be X or O and record their move on the board for each turn.
    - i.e. Print out the state of the board after each move.
- Make sure to consider some basic validations in your code like:
    - Player enters a spot that has been taken.
    - Invalid user input (non-digit or number out of bounds).
- The program will end when the board is filled up (no winner) or when there is a clear winner.
    - Output an end-of-game status message.
