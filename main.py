import random
import json
from datetime import datetime

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

def set_username(existing_status: bool, data: dict) -> str:
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
        
def initialize_game_list(data: dict, username: str) -> list:
    games = data.get(username, [])
    return games

def main() -> None:
    """Controls the main logic of the game"""
    data = import_data()
    welcome_message()
    existing_status = check_for_existing_user()
    username = set_username(existing_status, data)
    games = initialize_game_list(data, username)

def main_menu() -> str:
    """Takes player input to see if they want to play a round, see the stats or quit the game"""
    while True:
        player_choice = input("Do you want to play, see game stats, or quit (Enter p, s, or q): ").strip().lower()
        if player_choice in ("p", "s", "q"):
            return player_choice

def game_stats()



def computer_select() -> str:
    print("Computer making selection...")
    return random.choice(("rock", "paper", "scissors"))

def player_select() -> str:
    """Returns a string for the player selection input is mapped to a format that matches computer input"""
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

def create_timestamp() -> str:
    """Returns a string version of an isoformat datetime with millisecond precision"""
    timestamp = datetime.now().isoformat(timespec="milliseconds")
    return timestamp

def evaluate_winner(player_selection: str, computer_selection: str) -> str:
    """Returns the winner given a player selection and a computer selection"""
    if player_selection == computer_selection:
        return "tie"
    elif ((player_selection == "rock" and computer_selection == "scissors") or
            (player_selection == "paper" and computer_selection == "rock") or
            (player_selection == "scissors" and computer_selection == "paper")):
        return "player"
    return "computer"

def create_game_dictionary(timestamp: str, player_selection: str, computer_selection: str, winner: str) -> dict:
    """Creates a dictionary with the three crucial pieces of data for the current game"""
    return {
        "timestamp": timestamp,
        "player selection": player_selection,
        "computer selection": computer_selection,
        "winner": winner
    }

def append_game_dictionary(game_dictionary: dict, game_list: list) -> None:
    """Adds the current game data to the list of games for a given user"""
    game_list.append(game_dictionary)
    





