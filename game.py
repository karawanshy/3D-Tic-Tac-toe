class Game:
    def __init__(self):
        self.winning_combinations = [
            # Rows
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]
         
        self.current_player = ''
    
    def display_grid(self, grid):
        ''' 
        The function accepts one parameter containing one of the three grids's current status
        and prints it out to the console. 
        '''
        print("+-------+-------+-------+")
        for i in range(3):
            print("|       |       |       |")
            for j in range(3):
                print(f"|   {grid[i][j]}   ", end="")
            print("|\n|       |       |       |")
            print("+-------+-------+-------+")

    def display_board(self, board, ):
        '''
        The function accepts one parameter containing the board's current status
        and prints it out to the console.
        '''
        
        for i in range(3):
            print(f"\nGrid {i + 1}")
            self.display_grid(board[i])
   
    def check_tie(self, board):
        '''
        The function accepts one parameter containing the board's current status
        and checks whether there is a tie.
        '''

        for grid_index in range(3):
            for i in range(3):
                for j in range(3):
                    if board[grid_index][i][j] not in ['X', 'O']:
                        return False
        
        return True

    def victory_for(self, board):
        '''
        The function analyzes the board's status in order to check if 
        the player using 'O's or 'X's has won the game
        '''
        # check if a winning combination occurred
        for combo in self.winning_combinations:
            # we mark True each time we find the current player sign in the corresponding position in any of the three grids
            match_combo = {combo[0]: False, combo[1]: False, combo[2]: False}
            
            for grid_index in range(3):
                for cell in combo:
                    if board[grid_index][cell[0]][cell[1]] == self.current_player:
                        match_combo[cell] = True
            
            # check if all the cells in the combo has the current player sign - means a winning combination was found
            if all(value for value in match_combo.values()):
                return True
        
        # check if there is a cell in all three grids that matches the current sign - eg. (0, 0) cell is X in all three grids then it's a win
        for row in range(3):
            for col in range(3):
                if all(board[grid_index][row][col] == self.current_player for grid_index in range(3)):
                    return True
        
        return False

    def enter_move(self, board):
        '''
        The function accepts the board's current status, asks the current player about their move, 
        checks the input, and updates the board according to the user's decision.
        '''

        done = False
        while not done:
            try:
                grid, cell = map(int, input("\nPlease enter number of grid followed by number of cell: ").split())
            except (TypeError, ValueError):
                print("\nInvalid Input!")
            else:
                grid = int(grid) - 1 # to match the index
                cell = int(cell)

                if not (1 <= cell <= 9 and 0 <= grid <= 2):
                    print("Invalid grid or cell number!")
                else:
                    for i in range(3):
                        for j in range(3):
                            if board[grid][i][j] == cell:
                                board[grid][i][j] = self.current_player
                                self.display_board(board)
                                done = True
                    if not done:
                        print(f"Cell {cell} in grid {grid + 1} is already chosen!")

    def play_game(self, players):
        board = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

        self.display_board(board)

        # Updating the first player: If it is a fresh game or the last first player was 'O', then 'X' is the first player; otherwise, it is 'O'.
        self.current_player = 'X' if self.current_player != 'X' else 'O'
        print(self.current_player)

        while True:
            print(f"\nPlayer {self.current_player}'s turn...")
            self.enter_move(board)

            if self.victory_for(board):
                print(f"\nCongratulations, {players[self.current_player]} Won!")
                return self.current_player
            elif self.check_tie(board):
                print("\nGame's Over, It's a tie!")
                return None

            self.current_player = 'X' if self.current_player == 'O' else 'O'
