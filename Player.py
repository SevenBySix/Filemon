'''
this class will need to contain player data
a player object will have to include some sort of array or other dataset containing/representing
the players inventory.

Ultimately it would probobly be most simple for this class to work closest with the Save_Manager
class so our source code isnt full of attempts at working with files and writing.reading info


'''
from Save_Manager import Save_Manager

#player will need to hold a vertical location and its path, its name, filemon array

class Player(object):

    def __init__(self, directory, pos):
        self.currentDir = directory #THIS IS A STRING REPRESENTING A PATH
        self.position = pos #THIS IS A NUMBER CORRESPONDING TO HOW FAR DOWN IN THE PATH
        self.filemons = [] #The array of filemons
        self.previouslyEncountered = []
        self.inventory = ['Capture_Device', 'Healing_Device', 'Throwable_Rock', 'Camera', 'testThing1', 'testThing2', 'disposableThing', 'OtherDisposable'] #these are the basic items the player will have, more may be added or found depending on if time permits



    def writeToSave(self):
        Save_Manager.saveGame(self)

    #this will likely have to exist in some capacity, however player attributes can likely be
    #simply read from the save when the player object is initialized when the game is launched
    def readFromSave(self):
        self = Save_Manager.loadGame()

    def addFilemon(self, filemon):
        self.filemons.append(filemon)
        self.previouslyEncountered.append(filemon.path)
        self.position -=1





