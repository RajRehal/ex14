R = "rock"
P = "paper"
S = "scissors"

def user1():
    global user
    user = input("Choose R (rock), P (paper) or S (scissors)")
    if user == "R":
        print("You have selected " + R)
    if user == "P":
        print("You have selected " + P)
    if user == "S":
        print("You have selected " + S)
    return user
user1()

# computer
import random

def computer1():
    number = random.randint(0,2)
    computer_choices=["rock","paper","scissors"]
    global computer
    computer = computer_choices[number]
    print("Computer has selected " + computer)
    return computer
computer1()

# playgame
def playgame(user,computer):
    if user == computer:
        print("It's a tie")
    if user == "R":
        if computer == "paper":
            print("Computer has won")
        else:
            print("You have won")
    if user == "P":
        if computer == "scissors":
            print("Computer has won")
        else:
            print("You have won")
    if user == "S":
        if computer == "rock":
            print("Computer has won")
        else:
            print("You have won")

playgame(user,computer)