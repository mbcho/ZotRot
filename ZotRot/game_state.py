import locations as l
import characters as c
import functions as f

class GameState:
    def __init__(self):
        self.pastLocations = []
        self.currentLocation = None
        self.player = None

    def Game_Init(self):
        f.slow_print("Welcome to ZotRot, a UCI adventure!")
        f.slow_print("First of all, what's your name?")
        name = input(">> ")
        self.player = c.Player(name, 20)
        f.slow_print("Welcome to ZotRot " + self.player.name + "!!")
        print("-------------------------------------------------------")
        self.Location_Init()

    def Location_Init(self):
        # this sets up the graph, and initializes the current location to be the game's starting location
        Aldrich_Park = l.Location("\
It's another wonderful sunny afternoon at UCI! \
You're walking through Aldrich Park to get to your next class \
but you notice a few different things.\n",)
        Aldrich_Park_Left1 = l.Location("\
\"Umm hey dude! You doin alright?\" \
He lurches toward you... Dun dun dUN!!!", "SwagMan")
        ALP = l.Location("Wow what a great piece of architecture!")

        Aldrich_Park_Right1 = l.Location("Wow you moved to your right!")
        Aldrich_Park.addChildren([(Aldrich_Park_Left1, "To your left you see an old man stumbling through the park."),
                               (Aldrich_Park_Right1, "To your right you see something shiny hiding in the grass."),
                               (ALP, "In front of you is the Anteater Learning Pavilion!")])
        

        self.currentLocation = Aldrich_Park

        Student_Center = l.Location("You're in the student center")
        
    def Game_Loop(self):
        while (self.currentLocation != None):
            self.currentLocation = self.currentLocation.askPrompt()
            if (self.currentLocation.fight):
                self.player = self.currentLocation.Fight(self.player)

                
                
            
            
