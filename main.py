from game import Game
import random

def main():
    print("\n ======== Welcome to 3D Tic Tac Toe Game ======== \n")
    name1 = input("Please enter the name of the first player: ")
    name2 = input("Please enter the name of the second player: ")

    players = {'X':'', 'O':''}
    
    players['X'] = random.choice([name1, name2])
    players['O'] = name1 if players['X'] == name2 else name2

    print(f"\nPlayer X: {players['X']}      Player O: {players['O']}\n")

    while True:
        Game(players)
        choice = input("\nDo you want to play a new game? (Y/N) ").upper()
        if choice == 'N':
            break


if __name__=="__main__":
    main()

'''
Output Example:

 ======== Welcome to 3D Tic Tac Toe Game ======== 

Please enter the name of the first player: Red
Please enter the name of the second player: Green

Player X: Green      Player O: Red


Grid 1
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

Grid 2
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

Grid 3
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+

Player X's turn...

Please enter number of grid followed by number of cell:
'''
