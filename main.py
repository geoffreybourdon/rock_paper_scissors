import random
import json


data = {
    "Geoff": "games",
    "Bobby": "more games"
}

def import_data() -> dict:
    try:
        with open("rps_data.json") as f:
            data = json.laod(f)
    except FileExistsError:
        data = {}
    return data

def welcome_message() -> None:
    print("Welcome to Rock, Paper, Scissors!")

def check_for_existing_user() -> bool:
    """A function to demermine whether a user has an existing username"""
    while True:
        user_input = input("Do you have an existing user profile (y/n): ").strip().lower()
        if user_input in ("y", "n"):
            return user_input == "y"
        print("You must enter yes or no")

def set_username(existing_status: bool) -> str:
    while True:
        user_name = input("Enter your username: ").strip().title()
        if existing_status:
            if user_name in data.keys():
                print(f"Welcom back {user_name}")
                return user_name
            else:
                print("Your username was not found." 
                      "Would you like to try again or create a new account (retry/new): ")
                choice = input().strip().lower()
                if choice == "new":
                    print(f"Your username is {user_name}")
                    return user_name
        else:
            if user_name in data.keys():
                print("Your username is already in use. Please try a new name")
                continue
            print(f"Your username is {user_name}")
            return user_name
        
def initialize_game_list(user_name: str) -> list:
    games = data.get(user_name, [])


def computer_select() -> str:
    print("Computer making selection...")
    return random.choice(("rock", "paper", "scissors"))

def player_select() -> str:
    return_values = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }

    while True:
        player_selection = input("Make your selection (Enter r, p or s): ").strip().lower()
        if player_selection in ("r", "p", "s"):
            return return_values[player_selection]
        print("You must enter r, p, or s to select rock, paper, or scissors")





