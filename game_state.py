import locations as l
import characters as c
import functions as f
import sys, time, random

class GameState:
    def __init__(self):
        self.pastLocations = []
        self.currentLocation = None
        self.player = None
        self.joinGroup = False

    def Game_Init(self):
        print()
        print("\
███████╗ ██████╗ ████████╗██████╗  ██████╗ ████████╗\n\
╚══███╔╝██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝\n\
  ███╔╝ ██║   ██║   ██║   ██████╔╝██║   ██║   ██║   \n\
 ███╔╝  ██║   ██║   ██║   ██╔══██╗██║   ██║   ██║   \n\
███████╗╚██████╔╝   ██║   ██║  ██║╚██████╔╝   ██║   \n\
╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   \n")
        print()
                                                      
        f.slow_print("Welcome to ZotRot, a UCI adventure!")
        f.slow_print("First of all, what's your name?")
        name = input(">> ")
        self.player = c.Player(name, 20)
        f.slow_print("Welcome to ZotRot " + self.player.name + "!!")
        print("---------------------------------------------------------------------------------------------")
        self.Location_Init()

    def Location_Init(self):
        # this sets up the graph, and initializes the current location to be the game's starting location

# IMPLEMENT CONTINUE THING??????        
######################################################################################## Aldrich Park - start of game
        AldrichPark = l.Location("You find yourself in Aldrich Park, the peaceful green space at the heart of the University of California, \
Irvine. \nThe sun has set, and the park is quiet, but something feels off. You notice a strange figure in the distance, \
shuffling slowly towards you.\n", "ParkZombie")
        
        ICS1 = l.Location("As you look down at the undead body in front of you, the reality of the situation begins to sink in and \n\
you realize you need to find help. You look around and notice people running toward the ICS buildings; maybe there's something there. \n\
Scrambling up the terracotta-tinted steps, you painfully internalize the truth of the matter: \n\
you’re an outlier. Before the massive white structures before you stand the shambling remnants of your former colleagues, \n\
with death the beginning for them rather than the end. Their gazes, listless and glossed over. Their intellect, clouded, corrupted, \n\
discarded in favor of survival. All they need to do now is eat. And quite matter-of-factly, a previously haphazardly-seated zombie in \n\
particular has correctly identified the only food source in the area.\n", "ICSZombie")

        ALP = l.Location("You come up on the Anteater Learning Pavilion, wow what a great work of architecture!")
        StudentCenter = l.Location("You make your way to the Student Center and you begin to notice an awful smell...")

        AldrichPark.addChildren([(ICS1, "Continue...")])
######################################################################################## ALP - 
        # Humanities = l.Location("Old buildings with old book smells.")
        # Steinhaus = l.Location("You've never had a class here before... what even is this?")

        # ALP.addChildren([(BioSci, "BioSci is where I had my first class ever!!!"),
        #                 (Humanities, "Maybe Humanities will have a fix! Get it? Cuz human."),
        #                 (Steinhaus, "I have never been to Steinhaus Hall in my life... First time for everything!"),
        #                 (AldrichPark, "Go back to Aldrich Park")])
######################################################################################## Student Center
        # ArtSchool = l.Location("The Art School la la la")
        # FlagPoles = l.Location("The flag poles! Let's meet here!")
        # MiddleEarth = l.Location("Bring the ring to the volcano!")

        # StudentCenter.addChildren([(ArtSchool, "Let's go sing! The Art School!"),
        #                           (FlagPoles, "You see two big tall poles in the distance... Wanna dance?"),
        #                           (MiddleEarth, "Bilbo gives you a ring... Will you go to Middle Earth?"),
        #                           (AldrichPark, "Go back to Aldrich Park")])
######################################################################################## ICS
        
        SocialSci = l.Location("Social Sciences")
        
        InsideICS = l.Location("If there’s any way you’re getting out of this alive, it’s not going to be alone. \n\
Humans historically have gotten their way out of situations by combining their strengths, after all. And if that guy you just \n\
saw running past you is any bit sane still, it’s going to be the best you’ve got. He seems to have been sprinting for stairs \n\
at the ICS building. You’d better hurry before he gets too far ahead of you! As you fumble into the stairwell and shout after him, \n\
his panicked steps halt for a moment. “Another one? What’s your name?” You answer in kind. “Okay, that’s enough proof for me”, \n\
he says, running back down to shake your hand. “I’m Jerry. We can save the pleasantries for later. The building is secure for the most part; \n\
everyone that’s part of this small band of survivors is hard at work boarding up any windows and entrances. You’re lucky to have seen me run in \n\
the one entrance that’s not yet boarded up! Quickly, put this cart in front of the door then meet us all in the counselor’s office. Wasi says he \n\
knows a guy in Bio that might have an idea of what’s going on here. There might still be hope for us all!” As you supplant the supplies cart \n\
in the way of the door, you ponder this thought. ‘A guy in bio’… do they have a cure? You chuckle a bit at your miraculous luck and join the \n\
rest of the crew holed up in the conference room. As you enter the modestly-sized room on the third floor, Jerry waves you in and pats at a seat, \n\
the chairs arranged in a haphazard circle. “All right, y’all. This is a lucky survivor I found outside. Don’t worry, I made sure they’re clean. \n\
Their name is " + self.player.name + ". " + self.player.name + ", this is Dejian, Wasi, and Kyle. As far as I know, we’re the only survivors in this mess.” Wasi speaks up. \n\
“There’s supposed to be two more people here, Matt and Dharren, but they have already gone towards BioSci in order to prepare a station for a cure. \n\
Matt’s the one who has that knowledge and Dharren went to protect him. They don’t have all the materials yet; that’s what the two of them told us to \n\
get before joining them there. That was some time ago, though, so things have gotten much worse in the meantime. I hope they’re okay.” Dejian follows. \n\
“There are a few materials that we’ll need to make the cure. The idea is a back-mounted tank that holds the cure with a handheld nozzle. We’ll run \n\
around and spray the zombies with the cure! However, we’re going to need the materials for the cure, three things to be exact. Zombie flesh, \n\
Gas masks, and a Chemically-resistant spray tank. With the whole campus falling apart, we don’t really have a choice here; we’re going to have to \n\
split up.” Another survivor, Kyle, speaks up. “The zombie outbreak started at Rowland Hall, at least that’s what we think. \n\
If we’re going to find the most zombified flesh of all zombified flesh, it’s going to be there. Gas masks can be found in many different locations \n\
across the scientific side here, but the natural sciences building will have those in spades. A chemically-resistant spray tank is an oddity, \n\
but we should be able to find one in physical sciences.” He points to a scooter that’s standing at the side of the stand. He then looks at you. \n\
“That scooter’s mine but it might as well be ours at this point. It’s electric and big enough to carry two people, but it’s only got enough power \n\
to go to one of these places and back. It should get you past all the pathway shamblers without a problem, although I don’t think it’d be all that \n\
useful when fighting in the actual buildings. I’ll let you use it since you managed to survive getting here all alone unlike the rest of us. \n\
But where are you headed? You can go to Rowland Hall with Jerry, Natural Sciences with Dejian, or Physical Sciences with Wasi. Where are you going?\n")

        OutsideICS = l.Location("WHERE GO")
        # if self.joinGroup:
        ICS1.addChildren([(InsideICS, "Follow him?"),
                         (OutsideICS, "Stay away that's shady as hell...")])
        # else:
######################################################################################## BioSci - good ending requires materials
        # ChemLab = l.Location("It's the chemistry lab with lots of beakers, vials, and... meth?")
        # ScienceLibrary = l.Location("You see lots of weird books on the ground.", "FindBook")
      
        # BioSci.addChildren([(ChemLab, "You see a pair of double doors leading into an inconspicuous building."),
        #                    (Steinhaus, "I've never been to Steinhaus Hall in my life... First time for everything!"),
        #                    (ScienceLibrary, "Care for some light reading at the Science Library?"),
        #                    (ALP, "Go back to ALP")])
######################################################################################## Humanities
        # Humanities.addChildren([(FlagPoles, "Hey the flag poles are right there."),
        #                        (AldrichPark, "Apparently there are like 10,000+ trees in Aldrich"),
        #                        (ALP, "Go back to ALP")])
######################################################################################## Ring Road
        BioSci = l.Location("You approach BioSci and see a large, bald figure. Howard Gillman stands outside BioSci roaring in pleasure \n\
as he leaves the building with bags of cash. He seems to have kept his mind and is now towering over the zombified students. \n\
He becomes angry at their incompetence and slaughters them one by one. Soon there is only Gillman and his gold left.  Dejian shouts, \n\
“We have to fight him now while there is no other zombies around him.” The group launch their final attack.")

        # Split with Continue?
        RingRoad = l.Location("As they make their way through the Ring Road, they can hear the sound of growling and moaning in the distance. \n\
The once-bustling walkways are now filled with hordes of undead creatures, all searching for their next meal. The group moves cautiously, \n\
trying to avoid drawing attention to themselves, but it's becoming more and more difficult. The scent of humans seems to linger in the air, \n\
a reminder that the zombies are always close by. The group can't let their guard down for even a moment, knowing that one misstep could mean the \n\
end for them all. The trip to gather materials that was once a routine task has now become a perilous journey through a campus overrun by the undead. \n\
Despite the danger, the group knows that they must continue on and create a cure. \n", "Gloria Mark")

        RingRoad.addChildren([(BioSci, "Venture onward to BioSci! To the cure!")])

######################################################################################## ICS2
        ICSfromRowland = l.Location("You return to ICS and reconvene with the group gingerly holding your piece of rotting Zombie Flesh. \n\
You notice as you arrive that the other members of your group have already returned with Gas Masks and Chem Tanks. \n\
Jerry, Deijan, Wasi, and you have all made it back. Knowing it could be the last time you all are together, Deijan pours you all a glass of \n\
Zyr. You exchange stories about what happened, and hatch a plan to make it to BioSci. Everyone rests, and then heads out to BioSci.\n")

        ICSfromNatSci = l.Location("You return to ICS and reconvene with the group, your arms filled with as many Gas Masks as \n\
 you can hold. You notice as you arrive that the other members of your group have already returned with Zombie Flesh, and Chem Tanks. \n\
 Jerry, Deijan, Wasi, and you have all made it back. Knowing it could be the last time you all are together, Deijan pours you all a glass of \n\
 Zyr. You exchange stories about what happened, and hatch a plan to make it to BioSci. Everyone rests, and then heads out to BioSci.\n")
        
        ICSfromPhySci = l.Location("You return to ICS and reconvene with the group as you lug the heavy Chem Tank up the steps. \
You notice as you arrive that the other members of your group have already returned with Zombie Flesh and Gas Masks. \
Jerry, Deijan, Wasi, and you have all made it back. Knowing it could be the last time you all are together, Deijan pours you all a glass of \
Zyr. You exchange stories about what happened, and hatch a plan to make it to BioSci. Everyone rests, and then heads out to BioSci.\n")

        ICSfromRowland.addChildren([(RingRoad, "Continue to Ring Road")])
        ICSfromNatSci.addChildren([(RingRoad, "Continue to Ring Road")])
        ICSfromPhySci.addChildren([(RingRoad, "Continue to Ring Road")])

######################################################################################## Science Library - you get a book
        # ScienceLibrary.addChildren([(BioSci, "Go back to BioSci"),
        #                            (ALP, "Hey there's ALP! Full circle!")])

######################################################################################## Inside ICS - find group
        NaturalScience = l.Location("Dejian and you make it to Natural Sciences. On the way into the building, \n\
Deijan lays out the gameplan. The gas masks are in the basement. You need to make it down there, and back. \n\
There is the stairway, elevator, and emergency exit. He shows you the floor plan to make you understand the exits. Once you finish \n\
digesting the information, Deijan has one more surprise for you. He pulls out a bottle of Zyr vodka. Pours out two glasses and you \n\
toast to your health and success. You enter through the stairs, and find an axe stuck on the railing. As you journey deeper \n\
into the basement, you hear a howl. Unsure of what is instore, you signal Deijan to stay close, and then a shadow moves quickly in \n\
the distance. You try to see where it went and notice more shadows moving. The are getting closer and faster, \n\
and then they pounce.\n", "NatSciBoss")

        PhysicalScience = l.Location("Wasi and you dash to Physical Sciences. Upon arrival you realize you made a mistake to come here. \n\
The building is filled with zombies that are unlike anything either of you have seen before. They are all in the open surrounding \n\
the building dancing, hugging, and profusely moving their jaws. Their body compositions are fat but light. They are moving like \n\
brillant dancers yet are the size of sumo wrestlers. Unable to understand what is happening, Wasi and you hide in a bush where you \n\
find a crossbow with 24 arrows. Wasi and you realize that the zombies are partying, however they have no music. Wasi tells you to wait \n\
for his cue and begins sprinting to the Cafe Espresso across the quad. Moments pass, and you hear… ”BRING OUT THE LAZERS, \n\
BRING OUT THE LAZERS, BRING OUT THE LAZERS.” The zombies immediately head over banging their deformed heads. You sneak into the \n\
building. With your prior knowledge, you quickly find the tank and load it onto a cart. As you come back into the open, you see \n\
Wasi running to you. You notice the music has stopped, and the zombies are chasing 50 yards behind.\n", "SquirrelHorde")

        Rowland = l.Location("Jerry and you stealthily sneak into Rowland Hall. Jerry needs to take a piss, \n\
and you both navigate to the safest restroom you can find. As you enter the room, there is a deceased UCI student behind the door. \n\
With her eyes staring into Jerry’s, he could not contain it anymore. While Jerry is cleaning up, you examine the \n\
corpse and find a baseball bat with nails on its body. You quickly remove the weapon, and head out with Jerry. \n\
Terrified of being trapped on higher floors, you begin on the first floor. You are unable to find a dead zombie, and move into \n\
the second floor. You both question how this is possible. There should be zombies everywhere yet there are none. Floor by floor \n\
you make your way onto the fifth floor. Here the air is ominous. As you are clearing out a room, there is a shriek down the hall. \n\
You venture down the hall and discover what had happened.  A single zombie gained a mutation and started to get stronger with every \n\
zombie it ate. It feasted on the whole building and just finished off its last victim. You, shitting bricks, decide to retreat into \n\
the hallway. Jerry, the brave man he is, decides to lure it out into the open...\n", "RowlandBoss")

        InsideICS.addChildren([(Rowland, "Go to Rowland Hall"),
                               (NaturalScience, "Go to Natural Sciences"),
                               (PhysicalScience, "Go to Physical Sciences")])

######################################################################################## Rowland Hall - start of disease
        RowlandBasement = l.Location("Home of the nuclear reactor! Maybe that's what started this whole thing.")
        
        Rowland.addChildren([(RowlandBasement, "You see a door cracked open... kinda spooky but wanna check it out?"),
                             (ICSfromRowland, "Go back to ICS")])


######################################################################################## Natural Sciences
        NaturalScience.addChildren([(ICSfromNatSci, "Go back to ICS")])

######################################################################################## Physical Sciences
        PhysicalScience.addChildren([(ICSfromPhySci, "Go back to ICS")])

######################################################################################## 


######################################################################################## Init
        self.currentLocation = AldrichPark
        self.pastLocations.append(AldrichPark)

        
    def Game_Loop(self):
        while (self.currentLocation is not None):
            self.currentLocation.printDesc()
            if (self.currentLocation.event != None):
                self.player = self.currentLocation.event(self.player)
                if (self.player.check_dead()):
                    again = f.game_over()
                    if (again):
                        self.Game_Init()
                    else:
                        self.currentLocation = None

            self.currentLocation = self.currentLocation.askPrompt()

            if (self.currentLocation is None):
                if f.game_over():
                    self.Game_Init()
                else:
                    time.sleep(2)
                    quit()
                    
            self.pastLocations.append(self.currentLocation)

                
                
            
            
