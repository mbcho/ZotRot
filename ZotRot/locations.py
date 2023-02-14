import functions as f
import characters as c
import string

class Location:
    def __init__(self, desc, fight = None):
        self.desc = desc
        # self.alphabet = list(string.ascii_lowercase)[::-1]
        self.nums = ["4", "3", "2", "1"]
        self.options = {} #the children
        self.promptResponse = None
        self.fight = fight
        
    def addChild(self, childLoc, optionText:str):
        self.options[self.nums.pop()] = [childLoc, optionText]

    def displayPrompt(self):
        f.slow_print(self.desc)

        for letter, option in self.options.items():
            print("{}: {}".format(letter, option[1]))
            
    def addChildren(self, listOfChildren):
        for child in listOfChildren:
            self.options[self.nums.pop()] = [child[0], child[1]]

    def askPrompt(self): #returns next location
        self.displayPrompt()

        if not self.options:
            print("There are no options to go anywhere from here. THE END")
            return
            
        while self.promptResponse == None:
            response = input(">> ")
            if response in self.options:
                return self.options[response][0]
            print("That is not an available option!")

    def Fight(self, player):
        character = eval("c." + self.fight + "(player)")
        return character.fight()
