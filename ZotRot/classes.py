import functions

class Character:
    def __init__(self, name, maxhp):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.mentalhp = 10
        self.inventory = []
        self.status = []
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
            

class Game_State:
    def __init__(self, player):
        self.player = player

    def fight(self, enemy):
        if enemy == "Swag Man":
            self.Swag_Man()
        elif enemy == "Howard Gillman":
            self.Howard_Gillman()
            
    def Swag_Man(self):
        swag_man = Character("Swag Man", 30)
        action = ""
        while swag_man.alive == True:
            print("Quick! What do you do? (punch/kiss/run)")
            action = input(">> ")
            
            if action == "punch":
                print("You punch him in the face! It's so gooey.")
                swag_man.change_hp(-10)
                if (swag_man.check_dead() == True):
                    swag_man.alive = False
            elif action == "kiss":
                print("You give him a wet smooch and he bites your lip. Ouchy! Sexy!")
                self.player.change_hp(-1)
            elif action == "run":
                print("You turn around.")
            elif action == "stat":
                print("Current Health: " + str(self.player.hp))
            elif action == "thanos":
                self.player.change_hp(-10000000)
            if (self.player.check_dead() == True):
                functions.end_game()

        print("He falls to the ground twitching... That's what he gets!")

    def Howard_Gillman(self):
        howard_gillman = Character("Howard Gillman", 100)

        
class Player(Character):
    def __init__(self, name, maxhp):
        self.name = name
        self.hp = maxhp
        self.maxhp = 10
        self.location = ""
        self.inventory = []

    def change_location(self, location):
        self.location = location
        

class Howard_Gillman(Character):
    def __init__(self):
        self.name = "Howard Gillman"
        self.hp = 100
        self.maxhp = 100


    
