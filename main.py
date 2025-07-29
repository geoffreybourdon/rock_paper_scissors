import random
import json




data = {
    "Geoff": "games",
    "Bobby": "more games"
}

def welcome_message():
    print("Welcome to Rock, Paper, Scissors!")

def check_for_existing_user():
    """A function to demermine whether a user has an existing username"""
    while True:
        user_input = input("Do you have an existing user profile (y/n): ").strip().lower()
        if user_input in ("y", "n"):
            return user_input == "y"
        print("You must enter yes or no")

def set_username(existing_status):
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

print(set_username(check_for_existing_user()))


