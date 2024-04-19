# 3D-Tic-Tac-toe

Welcome to the 3D Tic Tac Toe Game! The game allows two players to play Tic Tac Toe in a 3x3x3 grid, adding an extra dimension to the classic game.

## How to Play

1. Upon starting the game, you will be prompted to enter the names of the two players.
2. The game will randomly assign 'X' and 'O' symbols to the players.
3. The players take turns entering their moves by specifying the grid number (1-3) followed by the cell number (1-9) where they want to place their symbol.
4. The game continues until one of the players wins or the game ends in a tie.
5. After each game, you will be asked if you want to play again.

## Rules

- Players take turns marking spaces in a 3x3x3 grid.
- The first player to achieve a winning combination horizontally, vertically, diagonally, or across the depth of the grid wins the game.
- If all spaces in the grid are filled and no player has won, the game ends in a tie.

## Additional Notes

- The game utilizes a `Game` class to manage the game logic and a `main` function to handle user interaction and game setup.
- The game includes error handling to ensure valid user inputs and provides informative error messages.
- The board is displayed to the console after each move, allowing players to visualize the progress of the game.

Enjoy playing the 3D Tic Tac Toe Game!
