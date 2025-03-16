from guessing_name import play
from rps8 import rps

def arcade(name = "Unknown"):
    question = input(f"\n {name} , Please press ...\n 1 for Rockpaperscissor\n 2 for guessing game")
    answer = int(question)

    if answer == 1:
        rock_paper_scissors = rps(name)
        rock_paper_scissors()
    elif answer == 2:
         game = play(name)
         game()
    else:
        return

    




import argparse
parser = argparse.ArgumentParser(
            description="Provides a personalized game experience."
        )

parser.add_argument(
            "-n", "--name", metavar="name",
            required=True, help="The name of the person playing the game." 
        )
args = parser.parse_args()
arc = arcade(args.name)
arc()