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