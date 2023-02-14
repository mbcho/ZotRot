import functions as f

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
        
    def fight(self):
        action = ""
        while self.alive == True:
            print("Quick! What do you do? (punch/kiss/run)")
            action = input(">> ")
            
            if action == "punch":
                print("You punch him in the face! It's so gooey.")
                self.change_hp(-10)
                if (self.check_dead() == True):
                    self.alive = False
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

        return self.player

class FirstZombie(Character):
    def __init__(self):
        super().__init__("Zombie", 5)

    def fight(self):
        print("ugh")
        
        
