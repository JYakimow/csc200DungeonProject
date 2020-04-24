import json

class Exit:
    def __init__(self, direction, destinationRoomID):
        self.direction = direction
        self.destinationRoomID = destinationRoomID
    
    def toJSON(self):
        aDictionary = {}
        aDictionary["direction"] = self.direction
        aDictionary["destinationRoomID"] = self.destinationRoomID
        return json.dumps(aDictionary)
        

def exitFromJson(self, jsonString):
    aDictionary = json.loads(jsonString)
    anExit = Exit(aDictionary["direction"], aDictionary["destionationRoomID"])
    return anExit


obj = {}
obj["title"] = "Cave Entrance"
obj["description"] = "A damp room"
obj["exits"] = []
obj["exits"].append(Exit("north", "R2"))
obj["exits"].append(Exit("south", "R1"))
print(obj)


for anExit in obj["exits"]:
    print(anExit.toJSON())

print(obj["title"])
jsonString = json.dumps(obj)
print(jsonString)

jsonString2 = '{"title": "Cave Entrance", "description": "A damp room", "exits": ["north", "south"]}'

theJsonFile = open("objTest.json")
jsonString3 = theJsonFile.read()
aDictionary = json.loads(jsonString3)

print(jsonString)
print(jsonString2)
print(jsonString3)



theObjectFile = open("objTest.json")
y = json.load(theObjectFile)
print(y["exits"][1])
print(aDictionary["exits"][0])