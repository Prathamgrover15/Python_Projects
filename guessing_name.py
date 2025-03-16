import sys
import random 
from enum import Enum
def play(name = "Unknown"):
    p_count = 0
    game_count = 0
    c_count = 0
    def play_play():
        nonlocal p_count
        nonlocal game_count
        nonlocal c_count
        p_choice = input(f"\n{name}, please enter a number 1,2 or 3 ")
        c_choice = random.choice("123")
        pl_choice = int(p_choice)
        co_choice = int(c_choice)
        print(f"\n{name} , you chose: " + p_choice)
        print(f"\nPython chose: " + c_choice)

        def decision(pl_choice,co_choice):
            nonlocal p_count
            nonlocal c_count
            if pl_choice == co_choice:
                p_count += 1
                return f"{name} you WIN."
            else:
                c_count += 1
                return "Python Wins"
            
        game_results = decision(pl_choice,co_choice)

        print(game_results)
        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s Wins: {p_count}")
        print(f"\nPython Wins: {c_count}")
        print(f"\nWinning Percentage: {(p_count/game_count)*100}")

        print(f"\nPLay Again?, {name}")

        while True:
            playagain = input(f"\nDo you wanna play again {name} Y or Q")
            if playagain.lower()  not in ["y","q"]:
                continue
                
            else:
                break

        if playagain.lower() == "y":
            return play_play()
        else:
            print("Thanks for playing\n")
            sys.exit("See you soon Boss")
        
                
    return play_play()
    
        
            

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game." 
    )

    args = parser.parse_args()

    game = play(args.name)
    game()