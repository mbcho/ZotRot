import sys, time, random

TYPING_SPEED = 500
VALID_INPUTS = ["1", "2", "3"]

def slow_print(string, wpm = TYPING_SPEED):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep((random.random()*10.0)/wpm)
    print()

def get_input():
    userInput = input(">> ")
    if (userInput not in VALID_INPUTS):
        print("Please enter a valid command.")
        get_input()
    else:
        return userInput
