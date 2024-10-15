from art import logo
from random import randint
print ("version 3")


def hard(the_number):
    print("You'll get five guesses\n")
    for i in range(5):
        user_input = int(input("guess the number :"))
        if user_input > the_number:
            print("You're to high")
        elif user_input < the_number:
            print("You're to low")
        elif user_input == the_number:
            print("You've got the number")
            break
        print(f"you've got {4-i} guesses left\n")
        if i == 4:
            print(f"the number was {the_number} you lose\n")


def easy(the_number):
    print("You'll get ten guesses\n")
    for i in range(10):
        user_input = int(input("guess the number :"))
        if user_input > the_number:
            print("You're to high")
        elif user_input < the_number:
            print("You're to low")
        elif user_input == the_number:
            print(f"You've got the number with {i+1} guesses")
            break
        print(f"you've got {9-i} guesses left\n")
        if i == 9:
            print(f"the number was {the_number} you lose\n")


def play():
    print(logo)
    the_number = randint(1, 100)
    value = input("guess the number i'm thinking of a number between 1 and 100\n"
                  "choose between 'hard' and 'easy' mode\n").lower()
    if value == "easy":
        easy(the_number)
    elif value == "hard":
        hard(the_number)

    while input("do you want to play again 'y' or 'n' ").lower() == "y":
        play()


play()
