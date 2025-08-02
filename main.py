import random
import json
from datetime import datetime
import pprint
import time

def import_data() -> dict:
    try:
        with open("rps_data.json") as f:
            data = json.laod(f)
    except FileNotFoundError:
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

def get_menu_choice() -> str:
    """Takes player input to see if they want to play a round, see the stats or quit the game"""
    while True:
        player_choice = input("Do you want to play, see game stats, or quit (Enter p, s, or q): ").strip().lower()
        if player_choice in ("p", "s", "q"):
            return player_choice

def calculate_stats(games: list[dict[str, str]]) -> dict[str, int]:
    stats = {
        "Wins": 0,
        "Losses": 0, 
        "Ties": 0, 
        "Rocks thrown": 0,
        "Papers thrown": 0,
        "Scissors thrown": 0
    }

    for game in games:
        throw = game.get("player choice")
        if throw == "rock":
            stats["Rocks thrown"] += 1
        elif throw == "paper":
            stats["Papers thrown"] += 1
        elif throw == "scissors":
            stats["Scissors thrown"] += 1
        
        winner = game.get("winner")
        if winner == "player":
            stats["Wins"] += 1
        elif winner == "computer":
            stats["Losses"] += 1
        elif winner == "tie":
            stats["Ties"] += 1
    
    return stats

def show_stats(username, stats: dict[str, int]) -> None:
    print(f"The stats for {username} are: ")
    pprint.pprint(stats, sort_dicts = False)


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

def show_winner(winner):
    print(f"The winner is....\n")
    time.sleep(.5)
    print(f"{winner}!!!")

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

def thank_you_message(username: str) -> None:
    print(f"Thank you for playing Rock, Paper, Scissors, {username}! Please Play again soon!")

def main() -> None:
    """Controls the main logic of the game"""
    data = import_data()
    welcome_message()
    existing_status = check_for_existing_user()
    username = set_username(existing_status, data)
    games = initialize_game_list(data, username)
    menu_choice = None
    while menu_choice != "q":
        menu_choice = get_menu_choice()
        if menu_choice == "s":
            stats = calculate_stats(games)
            show_stats(username, stats)
        else:
            computer_choice = computer_select()
            player_choice = player_select()
            timestamp = create_timestamp()
            winner = evaluate_winner(player_choice, computer_choice)
            game = create_game_dictionary(timestamp, player_choice, computer_choice, winner)
            append_game_dictionary(game, games)
    thank_you_message(username)

if __name__=="__main__":
    main()





