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
        self.mentalhp = 10
        self.inventory = []
        self.stats = {
        "attack": 1,
        "defense": 1,
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
                self.change_hp(-2)
            elif (action == "2"):
                f.slow_print("You approach him and ask if he needs help... He reaches for you and scratches you with his crusty nails..")
                self.player.change_hp(-1)
            elif (action == "3"):
                f.slow_print("YOU KICK HIM WHERE IT HURTS")
                self.change_hp(-3)
            if (self.player.check_dead()):
                f.slow_print("That's a zombie not some hungry dude! He eats you alive lol")
                return self.player
            if (self.check_dead()):
                    self.alive = False
                    break
            self.enemy_action()


        f.slow_print("The weird dude falls to the ground twitching... You approach the body and realize \
that's not some hungry dude that's a zombie!\n")

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
                self.change_hp(-20)
            elif (action == "2"):
                f.slow_print("Maybe a hug will heal all! He bites you.")
                # self.player.change_hp(-1)
            elif (action == "3"):
                f.slow_print("You ask him for help with your code. Nice.")
                # self.change_hp(-3)
            if (self.player.check_dead()):
                f.slow_print("You may have gotten away from the park zombie, but it seems your luck has \
very quickly and suddenly run out. With an unnatural sensation coursing through your veins as the zombie releases \
its bite, you feel… hungry. Ravenous. You must feed. Brains. Braaaaaaaaaaaaaiiiiiins.")
                return self.player
            if (self.check_dead()):
                self.alive = False
                break
            # self.enemy_action()


        f.slow_print("Fill\n")

        f.slow_print("With the rational mind taking control once again following the scuffle, you recall seeing someone \
running in a straight line in the background. It didn’t seem like they were one of them. Of course, there’s no way you \
were the ONLY survivor here! He seems to have been hocking a large amount of supplies. Perhaps he’s with some more normal people? \
You could follow him on the off chance that he happens to be part of a larger team. Then again, there’s a \
chance he’d think you’re a zombie and not want you following him. You also can’t be sure that he’s normal, either. \
Time is ticking. That one zombie you just felled was only one of many, and the scuffle you got into will surely attract more.")
        f.slow_print("Follow him or keep running?")
        return self.player

class RowlandBoss(Character):
    def __init__(self, player):
        super().__init__("Rowland Boss", 20)
        self.player = player

    def event(self):
        # GET BASEBALL BAT
        action = ""
        f.slow_print("Fight the big big one")
        while (self.alive):
            print("Professor Gopi's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Swing at him with the bat")
            print("2: Give him a bad score on RateMyProfessor")
            print("3: Present him a complicated math problem")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You punch him in the freaking face")
                self.change_hp(-1)
            elif (action == "2"):
                f.slow_print("Maybe a hug will heal all! He bites you.")
                self.player.change_hp(-1)
            elif (action == "3"):
                f.slow_print("You ask him for help with your code. Nice.")
                self.change_hp(-1)
            if (self.player.check_dead()):
                f.slow_print("Dang bro you died.")
                return self.player
            if (self.check_dead()):
                f.slow_print("You may have gotten away from the park zombie, but it seems your luck has \
very quickly and suddenly run out. With an unnatural sensation coursing through your veins as the zombie releases \
its bite, you feel… hungry. Ravenous. You must feed. Brains. Braaaaaaaaaaaaaiiiiiins.")
                self.alive = False
                break
            # self.enemy_action()

            f.slow_print("You defeat him and get his flesh yum")
            f.slow_print("***" + self.player.name + " has found: Zombie Flesh***\n")
            self.player.inventory.append("Zombie Flesh")

            return self.player

class NatSciBoss(Character):
    def __init__(self, player):
        super().__init__("Zombunnies", 30)
        self.player = player

    def event(self):
        # GET AXE
        action = ""
        f.slow_print("KILL THE STUPID  BUNNIES")
        while (self.alive):
            print("Zombunnie's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Stomp")
            print("2: Bat")
            print("3: Carrots?")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You punch him in the freaking face")
                self.change_hp(-1)
            elif (action == "2"):
                f.slow_print("Maybe a hug will heal all! He bites you.")
                self.player.change_hp(-1)
            elif (action == "3"):
                f.slow_print("You ask him for help with your code. Nice.")
                self.change_hp(-1)
            if (self.player.check_dead()):
                f.slow_print("Dang bro you died.")
                return self.player
            if (self.check_dead()):
                f.slow_print("You may have gotten away from the park zombie, but it seems your luck has \
very quickly and suddenly run out. With an unnatural sensation coursing through your veins as the zombie releases \
its bite, you feel… hungry. Ravenous. You must feed. Brains. Braaaaaaaaaaaaaiiiiiins.")
                self.alive = False
                break
            # self.enemy_action()

            f.slow_print("You defeat him and get gas masks")
            f.slow_print("***" + self.player.name + " has found: Gas Masks***\n")
            self.player.inventory.append("Gas Masks")

        return self.player

class SquirrelHorde(Character):
    def __init__(self, player):
        super().__init__("SQUIRRELS", 30)
        self.player = player

    def event(self):
        # GET AXE
        action = ""
        f.slow_print("KILL THE STUPID SWQAREUIAL")
        while (self.alive):
            print("Squirrel's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Stomp")
            print("2: Bat")
            print("3: Carrots?")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You punch him in the freaking face")
                self.change_hp(-1)
            elif (action == "2"):
                f.slow_print("Maybe a hug will heal all! He bites you.")
                self.player.change_hp(-1)
            elif (action == "3"):
                f.slow_print("You ask him for help with your code. Nice.")
                self.change_hp(-1)
            if (self.player.check_dead()):
                f.slow_print("Dang bro you died.")
                return self.player
            if (self.check_dead()):
                f.slow_print("You may have gotten away from the park zombie, but it seems your luck has \
very quickly and suddenly run out. With an unnatural sensation coursing through your veins as the zombie releases \
its bite, you feel… hungry. Ravenous. You must feed. Brains. Braaaaaaaaaaaaaiiiiiins.")
                self.alive = False
                break
            # self.enemy_action()

            f.slow_print("You defeat him and get Chemical Resistant Spray Tank")
            f.slow_print("***" + self.player.name + " has found: Chemical Resistant Spray Tank***\n")
            self.player.inventory.append("Chem Tank")

        return self.player

class GloriaMark(Character):
    def __init__(self):
        super().__init__("Glorai Mark", 50)

    def event(self):
        action = ""
        f.slow_print("KILL THE STUPID horde")
        while (self.alive):
            print("Horde's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: Stomp")
            print("2: Bat")
            print("3: Carrots?")

            action = f.get_input()

            if (action == "1"):
                f.slow_print("You punch him in the freaking face")
                self.change_hp(-1)
            elif (action == "2"):
                f.slow_print("Maybe a hug will heal all! He bites you.")
                self.player.change_hp(-1)
            elif (action == "3"):
                f.slow_print("You ask him for help with your code. Nice.")
                self.change_hp(-1)
            if (self.player.check_dead()):
                f.slow_print("Dang bro you died.")
                return self.player
            if (self.check_dead()):
                f.slow_print("You may have gotten away from the park zombie, but it seems your luck has \
very quickly and suddenly run out. With an unnatural sensation coursing through your veins as the zombie releases \
its bite, you feel… hungry. Ravenous. You must feed. Brains. Braaaaaaaaaaaaaiiiiiins.")
                self.alive = False
                break
            self.enemy_action()

            f.slow_print("You defeat him and get Chemical Resistant Spray Tank")
            f.slow_print("***" + self.player.name + " has found: Chemical Resistant Spray Tank***\n")
            self.player.inventory.append("Chem Tank")

        return self.player

    def enemy_action(self):
        print("Enemy attack here")

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
