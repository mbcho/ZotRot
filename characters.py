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
        "attack": 5,
        "defense": 5,
        "intelligence": 5,
        "charisma": 5,
        "luck": 0
        }

class SwagMan(Character):
    def __init__(self, player):
        super().__init__("Swag Man", 30)
        self.player = player
        
    def event(self):
        action = ""
        f.slow_print("You arrive at the ICS buildings and you notice a really \
swaggy looking man in a Bulls jersey stumble towards you...")
        while (self.alive):
            print("Swag Man's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))
            print("1: punch")
            print("2: kiss")
            print("3: run")
            action = f.get_input()
            
            if action == "1":
                f.slow_print("You punch him in the face! It's so gooey.")
                self.change_hp(-10)
            elif action == "2":
                f.slow_print("You give him a wet smooch and he bites your lip. Ouchy! Sexy!")
                self.player.change_hp(-100)
            elif action == "3":
                f.slow_print("You run away.")
                break
            if (self.player.check_dead()):
                return self.player
            if (self.check_dead()):
                    self.alive = False
                    break
            

            self.enemy_action()
                      
            

        if (self.hp == 0):
            f.slow_print("He falls to the ground twitching... That's what he gets!")
            f.slow_print("It looks really gross but do you want to take his awesome Bulls jersey?")
            print("1: HELL YEAH!")
            print("2: Eww no...")
            action = f.get_binary()

            if (action == "1"):
                f.slow_print("You put on his Bulls jersey... the inside is sticky.\n")
                f.slow_print("***" + self.player.name + " has found: Bulls Jersey***\n")
                self.player.inventory.append("Bulls Jersey")
                self.player.stats["defense"] += 1
                print(self.player.stats)
                print()
            elif (action == "2"):
                f.slow_print("Probably the right choice...\n")

        
        return self.player

    def enemy_action(self):
        action = random.choices(["1", "2"], [0.2, 0.8])
        if (action == ['1']):
            f.slow_print("He punches you in the freaking face!")
            self.player.change_hp(-1)
        elif (action == ['2']):
            f.slow_print("He just kinda stumbles around... Poor guy.")

        

class FirstZombie(Character):
    def __init__(self):
        super().__init__("Zombie", 5)

    def event(self):
        action = ""
        f.slow_print("You have to fight the Zombie!!!")
        while (self.alive):
            print("Swag Man's Current Health: " + str(self.hp) + "/" + str(self.maxhp))
            print(self.player.name + "'s Current Health: " + str(self.player.hp) + "/" + str(self.player.maxhp))

        
        
# class GloriaMark(Character):

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



