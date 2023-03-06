import random

def get_computer_choice():
    option_list = ["Rock", "Paper", "Scissors"]
    
    return random.choice(option_list)


def get_user_choice():
    user_choice = input("Enter your choice: ")

    return user_choice