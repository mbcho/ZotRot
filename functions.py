import sys, time, random

TYPING_SPEED = 50000
# VALID_INPUTS = ["1", "2", "3"]

def slow_print(string, wpm = TYPING_SPEED):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep((random.random()*10.0)/wpm)
    print()

def get_input(args = 3):
    VALID_INPUTS = []
    for i in range(1, args+1):
        VALID_INPUTS.append(str(i))

    userInput = input(">> ")
    print()
    if (userInput not in VALID_INPUTS):
        print("Please enter a valid command.")
        get_input()
    else:
        return userInput


def get_binary():
    userInput = input(">> ")
    print()
    if (userInput not in (["1","2"])):
        print("Please enter a valid command.")
        get_binary()
    else:
        return userInput

def game_over():
    slow_print("The game is over. Would you like to play again?")
    print("1: Yes")
    print("2: No")

    input = get_binary()

    if (input == "1"):
        return True
    elif (input == "2"):
        slow_print("Thank you for playing ZotRot! Have a nice life!")
        return False

