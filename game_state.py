import locations as l
import characters as c
import functions as f
import sys, time, random

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
        print("---------------------------------------------------------------------------------------------")
        self.Location_Init()

    def Location_Init(self):
        # this sets up the graph, and initializes the current location to be the game's starting location
        
######################################################################################## Aldrich Park - start of game
        AldrichPark = l.Location("\
It's another wonderful sunny afternoon at UCI! \
You're walking through Aldrich Park to get to your next class \
but you notice a few different things.\n")
        
        ICS = l.Location("You look around at the ICS buildings as you stand in the quad...", "SwagMan")
        ALP = l.Location("You come up on the Anteater Learning Pavilion, wow what a great work of architecture!")
        StudentCenter = l.Location("You make your way to the Student Center and you begin to notice an awful smell...")

        AldrichPark.addChildren([(ICS, "To your left you see the ICS buildings and you hear a commotion over there."),
                                 (StudentCenter, "To your right you see the road leading to the Student Center."),
                                 (ALP, "In front of you is the Anteater Learning Pavilion!")])
######################################################################################## ALP - 
        BioSci = l.Location("The Science Library towers over you.")
        Humanities = l.Location("Old buildings with old book smells.")
        Steinhaus = l.Location("You've never had a class here before... what even is this?")

        ALP.addChildren([(BioSci, "BioSci is where I had my first class ever!!!"),
                         (Humanities, "Maybe Humanities will have a fix! Get it? Cuz human."),
                         (Steinhaus, "I have never been to Steinhaus Hall in my life... First time for everything!"),
                         (AldrichPark, "Go back to Aldrich Park")])
######################################################################################## Student Center
        ArtSchool = l.Location("The Art School la la la")
        FlagPoles = l.Location("The flag poles! Let's meet here!")
        MiddleEarth = l.Location("Bring the ring to the volcano!")

        StudentCenter.addChildren([(ArtSchool, "Let's go sing! The Art School!"),
                                   (FlagPoles, "You see two big tall poles in the distance... Wanna dance?"),
                                   (MiddleEarth, "Bilbo gives you a ring... Will you go to Middle Earth?"),
                                   (AldrichPark, "Go back to Aldrich Park")])
######################################################################################## ICS
        Rowland = l.Location("Rowland Hall, home of the nuclear reactor **")
        SocialSci = l.Location("Social Sciences")
        
        ICS.addChildren([(Rowland, "You see Rowland Hall"),
                         (SocialSci, "Social Sciences"),
                         (AldrichPark, "Go back to Aldrich Park")])
######################################################################################## BioSci - good ending requires materials
        ChemLab = l.Location("It's the chemistry lab with lots of beakers, vials, and... meth?")
        ScienceLibrary = l.Location("You see lots of weird books on the ground.", "FindBook")
      
        BioSci.addChildren([(ChemLab, "You see a pair of double doors leading into an inconspicuous building."),
                            (Steinhaus, "I've never been to Steinhaus Hall in my life... First time for everything!"),
                            (ScienceLibrary, "Care for some light reading at the Science Library?"),
                            (ALP, "Go back to ALP")])
######################################################################################## Humanities
        
        Humanities.addChildren([(FlagPoles, "Hey the flag poles are right there."),
                                (AldrichPark, "Apparently there are like 10,000+ trees in Aldrich"),
                                (ALP, "Go back to ALP")])
######################################################################################## Steinhaus
            
        #Steinhaus.addChildren([(
######################################################################################## Rowland Hall - start of disease

        #Rowland_Hall.addChildren([(
######################################################################################## Science Library - you get a book
        ScienceLibrary.addChildren([(BioSci, "Go back to BioSci"),
                                    (ALP, "Hey there's ALP! Full circle!")])
########################################################################################
            

########################################################################################
            

########################################################################################
            

########################################################################################


######################################################################################## Init
        self.currentLocation = AldrichPark
        self.pastLocations.append(AldrichPark)

        
    def Game_Loop(self):
        while (self.currentLocation is not None):
            self.currentLocation = self.currentLocation.askPrompt()
            if (self.currentLocation is None):
                if f.game_over():
                    self.Game_Init()
                else:
                    time.sleep(2)
                    quit()
                    
            self.pastLocations.append(self.currentLocation)
            if (self.currentLocation.event != None):
                self.player = self.currentLocation.event(self.player)
                if (self.player.check_dead()):
                    again = f.game_over()
                    if (again):
                        self.Game_Init()
                    else:
                        self.currentLocation = None

                
                
            
            
