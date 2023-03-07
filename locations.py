import functions as f
import characters as c
import string

class Location:
    def __init__(self, desc, hasEvent = None):
        self.desc = desc
        # self.alphabet = list(string.ascii_lowercase)[::-1]
        self.pastLocations = []
        self.nums = ["4", "3", "2", "1"]
        self.options = {} #the children
        self.promptResponse = None
        self.hasEvent = hasEvent
        
    def addChild(self, childLoc, optionText:str):
        self.options[self.nums.pop()] = [childLoc, optionText]

    def printDesc(self):
        f.slow_print(self.desc)

    def displayPrompt(self):
        for num, option in self.options.items():
            print("{}: {}".format(num, option[1]))
            
    def addChildren(self, listOfChildren):
        for child in listOfChildren:
            self.options[self.nums.pop()] = [child[0], child[1]]

    def askPrompt(self): #returns next location

        self.displayPrompt()
        if not self.options:
            return
            
        while self.promptResponse == None:
            response = input(">> ")
            print()
            if response in self.options:
                self.pastLocations.append(self.options[response][0])
                return self.options[response][0]

            print("That is not an available option!\n")

    def event(self, player):
        if self.hasEvent != None:
            character = eval("c." + self.hasEvent + "(player)") 
            return character.event()
        return player
