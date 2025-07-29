import random
import json



class GameStatistics:
    def __init__(self):
        self.name = None
        self.games = []

    def load_data(self):
        try:
            with open("rps_data.json") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            data = {}

    def set_name():
        """Sets the user name for game statistics"""


def welcome_message():
    print("Welcome to Rock, Paper, Scissors!")

def check_for_existing_user():
    """A function to demermine whether a user has an existing username"""
    user_input = input("Do you have an existing user profile (y/n): ").strip().lower()
    validate_y_n(user_input)

def validate_y_n(some_string):
    """A function to make sure y or n was entered"""
    return

def get_y_n_input(message):
    while True:
        user_input = (f"{message} (y/n): ").strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid entry.")
            continue

check_for_existing_user()
print("done")