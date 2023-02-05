import classes as c
import functions as f
def Aldrich_Park_Start(game):
    directions = ["left", "right", "forward"]
    # f.slow_print("It's a beautiful sunny day in Aldrich Park! The birds are singing. But what's this?")
    print("It's a beautiful sunny day in Aldrich Park! The birds are singing. But what's this?")

    # f.slow_print("(1) To your left you see a poor old man stumbling in the grass.")
    print("(1) To your left you see a poor old man stumbling in the grass.")

    # f.slow_print("(2) To your right you see a beautiful patch of grass that looks perfect for napping.")
    print("(2) To your right you see a beautiful patch of grass that looks perfect for napping.")

    # f.slow_print("(3) In front of you, you see a coupon for a free drink at Cha.")
    print("(3) In front of you, you see a coupon for a free drink at Cha.")

    userInput = ""
    # f.slow_print("Would you like to move \"left\", \"right\", or \"forward\"?")

    userInput = f.get_input()

    if userInput == "1":
        print("Oh no! It's Swag Man and he's lookin at you like a snack!")
        game.Swag_Man()
        Aldrich_Park_Left1(game)
        
    elif userInput == "2":
        print("You fall asleep... You wake up to Gloria Mark eating you alive.")

    elif userInput == "3":
        print("You pick up the Cha coupon! Wow what a deal!")
        game.player.inventory.append("Cha coupon")
        

def Aldrich_Park_Left1(game):
    f.slow_print("Swag Man's dead, rotting body is laying at your feet. Yuck!")
    f.slow_print("(1) Search his body?")
    f.slow_print("(2) Continue forward.")
    f.slow_print("(3) Go back to where you started.")
