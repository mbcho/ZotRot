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
        
######################################################################################## Aldrich Park    
        Aldrich_Park = l.Location("\
It's another wonderful sunny afternoon at UCI! \
You're walking through Aldrich Park to get to your next class \
but you notice a few different things.\n")
        
        ICS = l.Location("\
You look around at the ICS buildings as you stand in the quad...", "SwagMan")
        
        ALP = l.Location("You come up on the Anteater Learning Pavilion, wow what a great work of \
architecture!")

        Student_Center = l.Location("You make your way to the Student Center and you begin to notice an awful smell.")

        Aldrich_Park.addChildren([(ICS, "To your left you see the ICS buildings and you hear a commotion over there."),
                                (Student_Center, "To your right you see the road leading to the Student Center."),
                                (ALP, "In front of you is the Anteater Learning Pavilion!")])
######################################################################################## ALP
        BioSci = l.Location("The Science Library towers over you.")
        Humanities = l.Location("Old buildings with old book smells.")
        Steinhaus = l.Location("You've never had a class here before... what even is this?")
        
        ALP.addChildren([(BioSci, "Blah"),
                         (Humanities, "Blah"),
                         (Steinhaus, "Blah")])
######################################################################################## Student Center
        
######################################################################################## ICS

######################################################################################## BioSci

######################################################################################## Humanities

######################################################################################## Steinhaus
        self.currentLocation = Aldrich_Park

        Student_Center = l.Location("You're in the student center")
        
    def Game_Loop(self):
        while (self.currentLocation != None):
            self.currentLocation = self.currentLocation.askPrompt()
            if (self.currentLocation.fight):
                self.player = self.currentLocation.Fight(self.player)

                
                
            
            
