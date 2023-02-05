import classes
import locations
import functions as f
import sys, time, random

TYPING_SPEED = 500
VALID_INPUTS = ["1", "2", "3"]

def game_init():
    f.slow_print("Welcome to ZotRot! A UCI adventure!")
    f.slow_print("Please enter your name!", 100)
    name = input(">> ")
    
    player = classes.Player(name, 15)
    f.slow_print("Thanks " + name + " for playing the game :)")

    print("------------------------------------------------------------")
    
    player.change_location("Aldrich Park")
    game_run(player)
    
def game_run(player):
    game = classes.Game_State(player)
    if player.location == "Aldrich Park":
        locations.Aldrich_Park_Start(game)
    
def end_game():
    f.slow_print("You died :(")
    f.slow_print("Try again? (yes / no)")
    action = input(">> ")
    if (action == "yes"):
        game_init()
    else:
        exit()

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


    
    
