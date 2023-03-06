import random

def get_computer_choice():
    option_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(option_list)
    
    return computer_choice


def get_user_choice():
    user_choice = input("Enter your choice: ")

    return user_choice


def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print("It is a tie!")

    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You won!")

    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You won!")

    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You won!")

    else:
        print("You lost")

