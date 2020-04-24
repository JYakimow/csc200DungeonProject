#drill homework 18

import json
import random

class Room:
    def __init__(self, title, description, roomID):
        self.title = title
        self.description = description
        self.listOfExits = []
        self.listOfInhabitants = []
        self.roomID  = roomID
    
    def display(self):
        print()
        print(f"{self.title}\n{self.description}")
       
        inhabitantsString = ""
        
        for anInhabitant in self.listOfInhabitants:
            inhabitantsString = inhabitantsString + anInhabitant.name + " "
        
        print(f"Also Here: {inhabitantsString}")
        
        exitString = ""
        for anExit in self.listOfExits:
            exitString = exitString + anExit.direction + " "
            
        print(f"Obvious Exits: {exitString}")
        print()
    
    def takeExit(self, aPlayer, aDirection):
        for anExit in self.listOfExits:
            if(anExit.direction == aDirection):
                self.listOfInhabitants.remove(aPlayer)
                anExit.roomDestination.addPlayer(aPlayer)
                
    def addExit(self, aExit):
        self.listOfExits.append(aExit)
    
    def addMonster(self, aMonster):
        self.listOfInhabitants.append(aMonster)
        
    def addPlayer(self, aPlayer):
        self.listOfInhabitants.append(aPlayer)
        aPlayer.setCurrentRoom(self)

    def kill(self, anInhabitant):
        self.listOfInhabitants.remove(anInhabitant)
        print(anInhabitant.name, "Has died")

class Exit:
    def __init__(self, direction, roomDestination):
        self.direction = direction
        self.roomDestination = roomDestination
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hitPoints = 10
        self.currentRoom = None
    
    def display(self):
        print(self.name)
    
    def setCurrentRoom(self, aRoom):
        self.currentRoom = aRoom
    
    def pAttack(self, enemy):
        temp = random.randint(0,100)
        if temp % 2 == 0:
            print("You miss the", enemy.name)
            print(self.name, "(", self.hitPoints,"HP)", enemy.name, " (", enemy.hitPoints,"HP)")
        else:
            enemy.hitPoints = enemy.hitPoints - 1
            print("You hit", enemy.name, "for 1 dmg")
            print(self.name, "(", self.hitPoints,"HP)", enemy.name, " (", enemy.hitPoints,"HP)")

class Monster:
    def __init__(self, name, hitPoints):
        self.name = name
        self.hitPoints = hitPoints

    def npcAttack(self, enemy):
        temp = random.randint(0,100)
        if temp % 2 == 0:
            print(self.name, "misses you")
            print(self.name, "(", self.hitPoints,"HP)", enemy.name, " (", enemy.hitPoints,"HP)")
        else:
            enemy.hitPoints = enemy.hitPoints - 1
            print(self.name, "hits", enemy.name, "for 1 dmg")
            print(self.name, "(", self.hitPoints,"HP)", enemy.name, " (", enemy.hitPoints,"HP)")

class MapBuilder:
    def __init__(self, fileName):
        self.theMapFile = open(fileName)
        self.theMapVar = json.load(self.theMapFile)
        #self.currentRoom = json.load(theMapFile)
        self.roomList = []
        self.exitList = []
        self.roomCounter = None
        self.counter = 0
        self.currentID = None
        self.exitCount = 0
        self.exitList = []

    def buildRooms(self):
        theTitle = None
        theDescription = None
        theID = None
        self.counter = 0
        for i in self.theMapVar:
            theTitle = i["title"]
            theDescription = i["description"]
            theID = i["ID"]
            self.currentID = theID
            self.roomCounter = theID
            self.roomCounter = Room(theTitle, theDescription, theID)
            self.roomList.append(self.roomCounter)
            count = 0
            for i in self.theMapVar[self.counter]["exits"]:
                destID = self.theMapVar[self.counter]["exits"][count]["destinationID"]
                direct = self.theMapVar[self.counter]["exits"][count]["direction"]
                self.exitCount = Exit(direct, destID)
                self.exitList.append(self.exitCount)
                count = count + 1
                #self.exitCount = self.exitCount + 1
            self.counter = self.counter + 1

    """def BuildExits(self):
        count = 0
        for i in self.theMapVar[self.counter]["exits"]:
            destID = self.theMapVar[self.counter]["exits"][count]["destinationID"]
            direct = self.theMapVar[self.counter]["exits"][count]["direction"]
            print(destID)
            print(direct)
            self.exitCount = Exit(direct, destID)
            self.currentID.addExit(self.exitCount)
            count = count + 1
            self.exitCount = self.exitCount + 1
            """
    def display(self):
        for aRoom in self.roomList:
            aRoom.display()

def main():   

    theMap = MapBuilder("theMap.json")
    theMap.buildRooms()
    print()
    #theMap = MapBuilder("theMap.json")
   # theMap.BuildExits()

    thePlayer = Player("[Mr. Gonzales]")
    R1.addPlayer(thePlayer)
    
    #Dragon = Monster("[Dragon]", 15)
    #R6.addMonster(Dragon)
    
    Rat = Monster("[Rat]", 3)
    R1.addMonster(Rat)

    while True:
        thePlayer.currentRoom.display()
        command = input("What would you like to do? : ")
        if(command == "quit"):
            break
        elif(command == "look"):
            continue
        elif command == "kill rat" or command == "attack rat":
            print()
            print("You position yourself to attack the Rat")
            print(thePlayer.name, "(", thePlayer.hitPoints,"HP)", Rat.name, " (", Rat.hitPoints,"HP)")
            while True:
                thePlayer.pAttack(Rat)
                Rat.npcAttack(thePlayer)
                if Rat.hitPoints == 0:
                    thePlayer.currentRoom.kill(Rat)
                    break 
                elif thePlayer.hitPoints == 0:
                    thePlayer.currentRoom.kill(thePlayer)
                    break
                else:
                    continue
            continue
        elif command == "kill dragon" or command == "attack dragon":
            print()
            print("You position yourself to attack the Dragon")
            print(thePlayer.name, "(", thePlayer.hitPoints,"HP)", Dragon.name, " (", Dragon.hitPoints,"HP)")
            while True:
                thePlayer.pAttack(Dragon)
                Dragon.npcAttack(thePlayer)
                if Dragon.hitPoints == 0:
                    thePlayer.currentRoom.kill(Dragon)
                    break
                elif thePlayer.hitPoints == 0:
                    thePlayer.currentRoom.kill(thePlayer)
                    break
                else:
                    continue
            continue
        else:
            thePlayer.currentRoom.takeExit(thePlayer, command)
    print("Goodbye!")

        
if __name__ == "__main__":
    main()
