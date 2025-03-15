import sys
import random # Choose something random
from enum import Enum # Enum is used for just converting the strings into some labels (which here are numbers)

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0 # All these are are added to just increase the count of the wins of python as well as the player and nonlocaling all of these to use in nested function.

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins


        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        playerchoice = input(f"\n{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
        
        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '')}.")
        print("Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        def define_winner(player,computer):
            nonlocal name
            nonlocal python_wins
            nonlocal player_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!" # use Windows key and period symbol to generate a emoji.
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..."
            
        game_result = define_winner(player,computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s Wins: {player_wins}")
        print(f"\nPython Wins: {python_wins}")      
            
        print(f"\nPLay Again?, {name}")
        
        while True:
            playagain = input("\nY for Yes \nQ to Quit \n\n")
            if playagain.lower() not in ["y","s"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing!\n")
            sys.exit("See you soon Boss")# This helps the code to end and also prints the statement mention afterwards.
        
    return play_rps

if __name__ == "__main__": #This will help to convert out file into a module and will only run when the file is the main file.

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game." # All of the above is just used to make the game more interactive and interact with the command line.
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
