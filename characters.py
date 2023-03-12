import functions as f
import random

class Character:
    def __init__(self, name, maxhp):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
   
        self.alive = True

    def change_hp(self, i):
        self.hp += i
        if self.hp < 0:
            self.hp = 0
        elif self.hp > self.maxhp:
            self.hp = self.maxhp

    def check_dead(self):
        if self.hp == 0:
            return True
        else:
            return False

class Player(Character):
    def __init__(self, name, maxhp):
        super().__init__(name, maxhp)
        self.inventory = []
        self.stats = {
        "attack": 1,
        "defense": 0,
        "intelligence": 1,
        "charisma": 1,
        "luck": 1
        }



# TO DO:
# Fill in story
# Fill in fights
# Implement Continue??
# Add text saying that you go to ICS after first fight
# Add text joining group and going to collect materials
# Finishing specifics of each fight



class ParkZombie(Character):
    def __init__(self, player):
        super().__init__("ParkZombie", 5)
        self.player = player

    def event(self):
        action = ""
        f.slow_print("He's lookin at you like a snack...")
        while (self.alive):
            print("Hungry Dude's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Slap")
            print("2: Ask if he needs help")
            print("3: Kick")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You give him a nice slap in the face.")
                self.change_hp(-(self.player.stats["attack"] + random.choices([0, 1, 2], [0.2, 0.5, 0.3])[0]))
            elif (action == "2"):
                f.slow_print("You approach him and ask if he needs help... He reaches for you and scratches you with his crusty nails..")
                self.player.change_hp(-(1 - self.player.stats["defense"]))
            elif (action == "3"):
                f.slow_print("YOU KICK HIM RIGHT WHERE IT HURTS!")
                self.change_hp(-(self.player.stats["attack"] + random.choices([0, 3, 4], [0.6, 0.2, 0.2])[0]))
            if (self.player.check_dead()):
                f.slow_print("That's a zombie not some hungry dude! He eats you alive lol")
                return self.player
            if (self.check_dead()):
                    self.alive = False
                    break
            self.enemy_action()


        f.slow_print("The weird dude falls to the ground twitching... You approach the body and realize \
that's not some hungry dude that's a zombie!\n")

        f.slow_print("He's wearing a cool jacket and some nice gloves...")
        print("1: Take jacket")
        print("2: Take gloves")
        action = f.get_binary()

        if (action == "1"):
            f.slow_print("***" + self.player.name + " has found: Thick Jacket***")
            f.slow_print("***Defense +1***\n")
            self.player.stats["defense"] += 1
        elif (action == "2"):
            f.slow_print("***" + self.player.name + " has found: Winter Gloves***")
            f.slow_print("***Attack +1***\n")
            self.player.stats["attack"] += 1

        return self.player

    def enemy_action(self):
        action = random.choices(["1", "2"], [0.5, 0.5])
        if (action == ['1']):
            f.slow_print("The dude growls at you angrily... What a weird guy.")
        elif (action == ['2']):
            f.slow_print("He stumbles around... You good?")

class ICSZombie(Character):
    def __init__(self, player):
        super().__init__("ICSZombie", 7)
        self.player = player

    def event(self):
        action = ""
        f.slow_print("Fight to survive!!!")
        while (self.alive):
            print("Zombie's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Punch")
            print("2: Big hug")
            print("3: Ask him for help with your ICS homework")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You punch him in the freaking face")
                self.change_hp(-(self.player.stats["attack"] + random.choices([0, 1, 2], [0.2, 0.5, 0.3])[0]))
            elif (action == "2"):
                f.slow_print("Maybe a hug will heal all! He bites you.")
                self.player.change_hp(-(2 - self.player.stats["defense"]))
            elif (action == "3"):
                f.slow_print("You ask him for help with your code. He doesn't know recursion!!!")
                self.change_hp(-(self.player.stats["attack"] + random.choices([0, 7], [0.8, 0.2])[0]))
            if (self.player.check_dead()):
                f.slow_print("You may have gotten away from the park zombie, but it seems your luck has \n\
very quickly and suddenly run out. With an unnatural sensation coursing through your veins as the zombie releases \n\
its bite, you feel… hungry. Ravenous. You must feed. Brains. Braaaaaaaaaaaaaiiiiiins.")
                return self.player
            if (self.check_dead()):
                self.alive = False
                break
            self.enemy_action()
        f.slow_print("He falls, killed for the second time.")
        f.slow_print("You notice the zombie is holding a nice laptop and wearing a nice cap.")
        print("1: Take laptop")
        print("2: Take cap")
        action = f.get_binary()

        if (action == "1"):
            f.slow_print("***" + self.player.name + " has found: Heavy Laptop***")
            f.slow_print("***Attack +1***\n")
            self.player.stats["attack"] += 1
        elif (action == "2"):
            f.slow_print("***" + self.player.name + " has found: Lakers Hat***")
            f.slow_print("***Defense +1***\n")
            self.player.stats["defense"] += 1

        f.slow_print("With the rational mind taking control once again following the scuffle, you recall seeing someone \n\
running in a straight line in the background. It didn’t seem like they were one of them. Of course, there’s no way you \n\
were the ONLY survivor here! He seems to have been hocking a large amount of supplies. Perhaps he’s with some more normal people? \n\
You could follow him on the off chance that he happens to be part of a larger team. Then again, there’s a \n\
chance he’d think you’re a zombie and not want you following him. You also can’t be sure that he’s normal, either. \n\
Time is ticking. That one zombie you just felled was only one of many, and the scuffle you got into will surely attract more.\n")
        f.slow_print("Follow him or keep running?")
        return self.player

    def enemy_action(self):
        action = random.choices(["1", "2"], [0.7, 0.3])
        if (action == ['1']):
            f.slow_print("He reaches out and scratches you! Yeeeowch!")
            self.player.change_hp(-(3-self.player.stats["defense"]))
        elif (action == ['2']):
            f.slow_print("He stumbles around... Can't touch this.")

class RowlandBoss(Character):
    def __init__(self, player):
        super().__init__("Rowland Boss", 20)
        self.player = player

    def event(self):
        # GETz BASEBALL BAT
        self.player.stats["attack"] += 2

        action = ""
        f.slow_print("Fight the Zombie Gopi!")
        while (self.alive):
            print("Professor Gopi's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Swing at him with the bat")
            print("2: Give him a bad score on RateMyProfessor")
            print("3: Present him a complicated math problem")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("Hey batter batter SWING!!\n")
                self.change_hp(-(self.player.stats["attack"] + random.choices([1, 2, 3], [0.2, 0.5, 0.3])[0]))
            elif (action == "2"):
                temp = random.choices([0, 20], [0.9, 0.1])[0]
                if temp == 0:
                    f.slow_print("Just one rating among many!!!\n")
                    self.change_hp(-1)
                elif temp == 20:
                    f.slow_print("\"NOO 0% WOULD TAKE MY CLASS AGAIN\" he wails as he melts into a puddle of sadness.\n")
                    self.change_hp(-20)
            elif (action == "3"):
                f.slow_print("He takes a moment to think and you whack him!\n")
                self.change_hp(-(self.player.stats["attack"] + random.choices([2, 4, 6], [0.8, 0.1, 0.1])[0]))
            if (self.player.check_dead()):
                f.slow_print("You fall to the ground and can do nothing as the zombified Professor Gopi lumbers towards you. \n\
As he hungrily places you into his mouth your consciousness fades... *GULP*")
                return self.player
            if (self.check_dead()):
                self.alive = False
                break

            self.enemy_action()

        f.slow_print("You defeat him and retrieve a small piece of his flesh. Yummy!")
        f.slow_print("***" + self.player.name + " has found: Zombie Flesh***\n")
        self.player.inventory.append("Zombie Flesh")

        return self.player

    def enemy_action(self):
        action = random.choices(["1", "2", "3"], [0.6, 0.2, 0.2])
        if (action == ['1']):
            f.slow_print("He hurls a big rock at you!!")
            self.player.change_hp(-(3 - self.player.stats["defense"]))
        elif (action == ['2']):
            f.slow_print("He spews acid at you out of his nose!!")
            self.player.change_hp(-(1 + random.choices([1, 2, 3], [0.33, 0.33, 0.33])[0] - self.player.stats["defense"]))
        elif (action == ['3']):
            f.slow_print("PROFESSOR GOPI THROWS A RADIOACTIVE ROCK AT YOU WATCH OUT!!!")
            chance = random.choices([1, 2], [0.1, 0.9])[0]
            if (chance == 1):
                f.slow_print("IT HITS YOU AHHHHHHHH")
                self.player.change_hp(-(10 - self.player.stats["defense"]))
            elif (chance == 2):
                f.slow_print("You lunge out of the way. Phew!")

class NatSciBoss(Character):
    def __init__(self, player):
        super().__init__("Zombunnies", 30)
        self.player = player

    def event(self):
        f.slow_print("You notice a forgotten pair of track shoes. Did you know they have spikes?")
        print("***" + self.player.name + " has found: Track Spikes***")
        print("***Attack +1, Defense +1***")
        self.player.stats["attack"] += 1
        self.player.stats["defense"] += 1

        action = ""
        f.slow_print("KILL THE STUPID BUNNIES")
        while (self.alive):
            print("Zombunnie's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Stomp")
            print("2: Try to hit them with your bat")
            print("3: Carrots?")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You stomp your spiked feet and feel crunching...")
                self.change_hp(-(self.player.stats["attack"] + random.choice([2, 3, 5], [0.33, 0.33, 0.33])[0]))

            elif (action == "2"):
                chance = random.choice([1, 2], [0.5, 0.5])[0]
                if chance == 1:
                    f.slow_print("You swing and swing with your bat but the targets are too small and too many!")
                elif chance == 2:
                    f.slow_print("You sweep your bat along the ground and hit some of them!")
                    self.change_hp(-(self.player.stats["attack"]))

            elif (action == "3"):
                f.slow_print("You throw some old carrot sticks on the ground...")
                chance = random.choice([1, 2], [0.4, 0.6])[0]
                if chance == 1:
                    f.slow_print("The zombunnies are hungry for MEAT! They lunge at you.")
                    self.player.change_hp(-(5 - self.player.stats["defense"]))
                elif chance == 2:
                    f.slow_print("Some of the zombunnies forget that they're carnivores and get distracted.")
                    self.change_hp(-(random.choice([4, 5, 6], [0.33, 0.33, 0.33])[0]))

            if (self.player.check_dead()):
                f.slow_print("You fall to the ground, unable to do anything as the zombunnies begin to pile on top of you \
and consume.")
                return self.player
            if (self.check_dead()):
                self.alive = False
                break
            self.enemy_action()

            f.slow_print("You defeat him and get gas masks")
            f.slow_print("***" + self.player.name + " has found: Gas Masks***\n")
            self.player.inventory.append("Gas Masks")

        return self.player

    def enemy_action(self):
        action = random.choices(["1", "2", "3"], [0.6, 0.3, 0.1])
        if (action == ['1']):
            f.slow_print("The zombunnies nibble at your little toes!")
            self.player.change_hp(-(3 + random.choice([3, 4, 5], [0.33, 0.33, 0.33])[0] - self.player.stats["defense"]))
        elif (action == ['2']):
            f.slow_print("The zombunnies lunge... They're closing in!")
        elif (action == ['3']):
            f.slow_print("The zombunnies have reached you!!! NOOOOOOO OUCH THE ZOMBUNNY BARRAGE!")
            self.player.change_hp(-(10 - self.player.stats["defense"]))

class BloatedHorde(Character):
    def __init__(self, player):
        super().__init__("Bloated Horde", 30)
        self.player = player
        self.distance = 50
        self.bolts = 24

    def event(self):
        # GET AXE
        action = ""
        f.slow_print("Escape the zombie horde!")
        while (self.alive):
            print("Bloated Horde's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print("Bloated Horde's Distance: " + str(self.distance) + " yards")
            print("Remaining Bolts: " + str(self.bolts))
            print("1: Fire crossbow")
            print("2: Retreat back")
            print("3: Poke them with a long fingernail")

            action = f.get_input()

            if (action == "1"):
                dmg = random.choices([3, 4, 5], [0.33, 0.33, 0.33])[0]
                f.slow_print("You fire a cross bow bolt, piercing " + str(dmg) + " of their bodies and they explode")
                self.change_hp(-dmg)
                self.bolts -= 1
            elif (action == "2"):
                distanceBack = random.choices([1, 2, 3], [0.3, 0.2, 0.5])[0]
                f.slow_print("You retreat back " + str(distanceBack) + " yards")
                self.distance += distanceBack
            elif (action == "3"):
                f.slow_print("You reach forward and poke one of the zombies with a long fingernail and he explodes splashing all over you.")
                self.change_hp(-1)
                self.player.change_hp(-(random.choices([3, 4, 5], [0.33, 0.33, 0.33])[0] - self.player.stats["defense"]))
            if (self.player.check_dead()):
                f.slow_print("As the zombie's toxic innards are splashed on top of you, your vision begins to fade and you can only \n\
watch helplessly as they descend upon you...")
                return self.player
            if (self.check_dead()):
                self.alive = False
                break
            if (self.distance <= 0):
                f.slow_print("The bloated horde has reached you and everything fades as they begin their feast...")
                self.player.change_hp(-999)
                return self.player
            self.enemy_action()

        print()
        f.slow_print("You defeat the horde and get Chemical Resistant Spray Tank")
        f.slow_print("***" + self.player.name + " has found: Chemical Resistant Spray Tank***\n")
        self.player.inventory.append("Chem Tank")

        return self.player

    def enemy_action(self):
        distanceForward = random.choices([5, 7, 20], [0.2, 0.75, 0.05])[0]
        f.slow_print("The horde rushes forward another " + str(distanceForward) + " yards!")
        self.distance -= distanceForward

class GloriaMark(Character):
    def __init__(self, player):
        super().__init__("Gloria Mark", 50)
        self.player = player
        self.patience = 3

    def event(self):
        action = ""
        f.slow_print("Fight the professor!!!\n")
        while (self.alive):
            print("Professor Mark's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Group attack!!")
            print("2: Display poor project management")
            print("3: Participate in class :)")

            action = f.get_input()

            if (action == "1"):
                n = random.choices([1, 2, 3, 4, 5], [0.2, 0.1, 0.3, 0.3, 0.1])[0]
                f.slow_print("The five of you attack all at once!! " + str(n) + " of your attacks hit!")
                self.change_hp(-(n * 2))
            elif (action == "2"):
                f.slow_print("She cringes at your awful display of mismanagement!")
                n = random.choices([3, 4, 5], [0.33, 0.33, 0.33])[0]
                self.change_hp(-n)
            elif (action == "3"):
                f.slow_print("You participate well in class. Her patience is sated!")
                self.patience = 2
            if (self.player.check_dead()):
                f.slow_print("Dang bro you died.")
                return self.player
            if (self.check_dead()):
                self.alive = False
                break
            self.enemy_action()

        f.slow_print("You defeat her Professor Mark and finally you can make your way to BioSci! You notice she was carrying \n\
some food with her and you take it for yourself.")
        f.slow_print("***" + self.player.name + "'s health has been restored!")
        self.player.change_hp(100)
        return self.player

    def enemy_action(self):
        n = random.choices([1, 2, 3], [0.5, 0.25, 0.25])[0]
        if (n == 1):
            f.slow_print("Professor Mark is losing patience...")
            self.patience -= 1
            if (self.patience == 0):
                f.slow_print("The Professor has lost her patience!!! Yeeeeowch!")
                self.player.change_hp(-(7 - self.player.stats["defense"]))
        elif (n == 2):
            f.slow_print("Professor Mark presents you with a Project Management question!\n")
            self.ask_question()

    def ask_question(self):
        n = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])[0]
        if (n == 1):
            f.slow_print("What is a temporary endeavor undertaken to create a unique product, service, or results?")
            print("1: system")
            print("2: project")
            print("3: product")
            
            answer = f.get_input()

            if (answer != "2"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 2):
            f.slow_print("What are the three elements of the triple constraint?")
            print("1: scope, time, cost")
            print("2: scope, energy, employees")
            print("3: risks, time, energy")
            
            answer = f.get_input()

            if (answer != "1"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 3):
            f.slow_print("Which of the following is not part of the three-sphere model for systems management?")
            print("1: business")
            print("2: information")
            print("3: organization")
            
            answer = f.get_input()

            if (answer != "2"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 4):
            f.slow_print("A ____________ is a series of actions directed toward a particular result.")
            print("1: goal")
            print("2: project")
            print("3: process")
            
            answer = f.get_input()

            if (answer != "3"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 5):
            f.slow_print("A ____________ is a document that formally recognizes the existence of a project and provides direction on \n\
the project’s objectives and management.")
            print("1: project charter")
            print("2: contract")
            print("3: business case")
            
            answer = f.get_input()

            if (answer != "1"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 6):
            f.slow_print("A ____________ is a deliverable-oriented grouping of the work involved in a project that defines its total scope.")
            print("1: WBS")
            print("2: work package")
            print("3: scope statement")
            
            answer = f.get_input()

            if (answer != "1"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 7):
            f.slow_print("What symbol on a Gantt chart represents a slipped milestone?")
            print("1: a black diamond")
            print("2: a white arrow")
            print("3: a white diamond")
            
            answer = f.get_input()

            if (answer != "3"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 8):
            f.slow_print("What is the main goal of project cost management?")
            print("1: to complete a project within an approved budget")
            print("2: to complete a project for as little cost as possible")
            print("3: to ensure that an organization’s money is used wisely")
            
            answer = f.get_input()

            if (answer != "1"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 9):
            f.slow_print("What does the term kaizen mean?")
            print("1: improvement")
            print("2: minimize waste")
            print("3: do it right the first time")
            
            answer = f.get_input()

            if (answer != "1"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")

        elif (n == 10):
            f.slow_print("What are the five stages in Tuckman’s model of team development, in chronological order?")
            print("1: forming, storming, norming, performing, and adjourning")
            print("2: norming, forming, storming, performing, and adjourning")
            print("3: forming, storming, performing, norming, and adjourning")
            
            answer = f.get_input()

            if (answer != "1"):
                print("That is incorrect!!!")
                self.player.change_hp(-(5 - self.player.stats["defense"]))
            else:
                print("Professor Mark is pleased by your answer.")


# class SuperZombie(Character):

# class Chemist(Character):

class FindBook(Character):
    def __init__(self):
        super().__init__("Book", 1)

    def event(self):
        action = ""
        f.slow_print("You see a bunch of books lying on the ground... Wanna grab one?")
        print("1: Sure! I like reading.")
        print("2: NOOOOO GET IT AWAY!!!!!!")
        action = f.get_binary()
        
        if action == "1":
            f.slow_print("You pick it up and take a look. Mollecular Physics Vol. 2.")
            f.slow_print("***" + self.player.name + " has found: Thick Book***\n")
            self.player.inventory.append("Thick Book")
            self.player.stats["attack"] += 1
        elif (action == "2"):
            f.slow_print("AAAAAAAAAHHHHHHHHHHHHHHH EVIL EVIL EVIL")

class Group(Character):
    def __init__(self):
        super().__init__("Group", 1)

    def event(self):
        action = ""
        f.slow_print("\"Hey! Cum cum cum!\", you walk up to the group of people")
        f.slow_print("Join them?")
        print("1: Yeah I love friends! <3")
        print("2: No I'm a lonely loser!")
        action = f.get_binary()

        if action == "1":
            f.slow_print("Blah")
            self.player.joinGroup = True
            f.slow_print("Alright we need to find 3 things in order to make the cure.")

        elif (action == "2"):
            f.slow_print("Bluh")
            self.player.joinGroup = False

class Continue(Character):
    def __init__(self, player):
        super().__init__("Continue", 1)
        self.player = player

    def event(self):
        action = ""
        f.slow_print("Input anything to continue...")
        input()

        return self.player
