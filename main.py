import random
import json
from datetime import datetime
import pprint

def import_data() -> dict:
    """Import the saved game data if it exists or create a blank dictionary"""
    try:
        with open("rps_data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

def welcome_message() -> None:
    """Welcome the player to the game"""
    print("Welcome to Rock, Paper, Scissors!")

def check_for_existing_user() -> bool:
    """Get user input to determine whether or not they have an existing profile"""
    while True:
        user_input = input("\nDo you have an existing user profile (y/n): ").strip().lower()
        if user_input in ("y", "n"):
            return user_input == "y"
        print("\nYou must enter yes or no")

def set_username(existing_status: bool, data: dict) -> str:
    """Verify existing profile status and set the username"""
    while True:
        user_name = input("\nEnter your username: ").strip().title()
        if existing_status:
            if user_name in data.keys():
                print(f"\nWelcom back {user_name}")
                return user_name
            else:
                print("\nYour username was not found." 
                      "Would you like to try again or create a new account (retry/new): ")
                choice = input().strip().lower()
                if choice == "new":
                    print(f"\nYour username is {user_name}")
                    return user_name
        else:
            if user_name in data.keys():
                print("\nYour username is already in use. Please try a new name")
                continue
            print(f"\nYour username is {user_name}")
            return user_name
        
def initialize_game_list(data: dict, username: str) -> tuple[list, dict]:
    """Retrieve the game list or create a new one and associate that list with the username in the data dictionary"""
    games = data.get(username, [])
    data[username] = games
    return games, data

def get_menu_choice() -> str:
    """Take player input to see if they want to play a round, see the stats or quit the game"""
    while True:
        player_choice = input("\nDo you want to play, see game stats, or quit (Enter p, s, or q): ").strip().lower()
        if player_choice in ("p", "s", "q"):
            return player_choice

def calculate_stats(games: list[dict[str, str]]) -> dict[str, int]:
    """Count the player stats from all the games in the game list"""
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
    """Print a summary of the player stats"""
    print(f"\nThe stats for {username} are: ")
    pprint.pprint(stats, sort_dicts = False)


def computer_choose() -> str:
    """Simulate a computer choosing rock, paper, or scissors"""
    print("\nComputer making selection...")
    return random.choice(("rock", "paper", "scissors"))

def player_choose() -> str:
    """Return a string for the player choice input is mapped to a format that matches computer input"""
    return_values = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }

    while True:
        player_choice = input("\nMake your selection (Enter r, p or s): ").strip().lower()
        if player_choice in ("r", "p", "s"):
            return return_values[player_choice]
        print("\nYou must enter r, p, or s to select rock, paper, or scissors")

def create_timestamp() -> str:
    """Return a string version of an isoformat datetime with millisecond precision"""
    # Will serve as unique identifier for each game. Can be used for some sorting stats in the future if desired
    timestamp = datetime.now().isoformat(timespec="milliseconds")
    return timestamp

def evaluate_winner(player_choice: str, computer_choice: str) -> str:
    """Return the winner given a player choice and a computer choice"""
    if player_choice == computer_choice:
        return "tie"
    elif ((player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")):
        return "player"
    return "computer"

def show_winner(computer_choice: str, player_choice: str, winner: str) -> None:
    """Display the throws for the round and who won"""
    print(f"\nThe computer chose {computer_choice} and you chose {player_choice}\n")
    if winner == "player":
        print("You Win!")
    elif winner == "computer":
        print("You lose!")
    else:
        print("It was a tie!")

def create_game_dictionary(timestamp: str, player_choice: str, computer_choice: str, winner: str) -> dict:
    """Create a dictionary with the data for the current game"""
    return {
        "timestamp": timestamp,
        "player choice": player_choice,
        "computer choice": computer_choice,
        "winner": winner
    }

def save_data(data):
    """Save a copy of the game data"""
    with open("rps_data.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)

def thank_you_message(username: str) -> None:
    """Thank player for playing by name"""
    print(f"\nThank you for playing Rock, Paper, Scissors, {username}! Please Play again soon!")

def main() -> None:
    """Controls the main logic of the game"""
    data = import_data()
    welcome_message()
    existing_status = check_for_existing_user()
    username = set_username(existing_status, data)
    games, data = initialize_game_list(data, username)
    menu_choice = None
    while menu_choice != "q":
        menu_choice = get_menu_choice()
        if menu_choice == "s":
            stats = calculate_stats(games)
            show_stats(username, stats)
        elif menu_choice == "p":
            computer_choice = computer_choose()
            player_choice = player_choose()
            timestamp = create_timestamp()
            winner = evaluate_winner(player_choice, computer_choice)
            show_winner(computer_choice, player_choice, winner)
            game = create_game_dictionary(timestamp, player_choice, computer_choice, winner)
            games.append(game)

    save_data(data)
    thank_you_message(username)

if __name__=="__main__":
    main()





