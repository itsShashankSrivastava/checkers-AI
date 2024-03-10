**Description: Checkers AI using Pygame and Alpha-Beta Pruning** 

This project is an implementation of the classic game of Checkers with an AI opponent using the Pygame library. The AI is designed to work either on Alpha-Beta Pruning algorithm or minimax algorithm. The game features a graphical user interface created with Pygame, allowing users to play against an intelligent computer opponent.

**Project Structure:**

main.py: The main entry point for the application. It initializes the Pygame window, handles user input, and controls the game loop. The AI opponent uses the Alpha-Beta Pruning algorithm to make strategic moves.

**checkers folder:**

board.py: Defines the Checkers game board, including methods for drawing the board, evaluating the game state, and managing piece movements.
constants.py: Contains constants such as window dimensions, square size, and colors used throughout the project.
game.py: Manages the overall game state, player turns, and interactions between the board and the user or AI opponent.
piece.py: Represents the game pieces (checkers) with methods for drawing, moving, and promoting to kings.

**alphaBeta folder:**

alphaBetaPruning.py: Implements the Alpha-Beta Pruning algorithm for the AI opponent. It evaluates possible moves using a heuristic and performs pruning to optimize the search process.
assets folder:

Contains the image of the crown used to represent king pieces.

**algorithms folder:**

minimax.py: An alternative implementation of the game's AI using the Minimax algorithm. This file is separate from the Alpha-Beta Pruning implementation, providing users with the option to choose the AI algorithm.

**How to Run:**

Ensure Python and Pygame are installed.
Run the main.py file to start the game.
Play against the AI or another human player.

**Features:**

Classic Checkers gameplay with a graphical user interface.
AI opponent using the Alpha-Beta Pruning algorithm for intelligent moves.
Option to use the Minimax algorithm as an alternative AI strategy.
Visual representation of valid moves during gameplay.

**Conclusion**

Comparative Analysis of both algorithms was the main motive for this game development. The time taken per move for Alpha Beta was much lesser than minimax, which can be clearly seen while implementing the game at any depth.


Feel free to explore, contribute, and provide feedback to enhance this Checkers game implementation!
