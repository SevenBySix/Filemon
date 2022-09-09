'''
this class will need to contain player data
a player object will have to include some sort of array or other dataset containing/representing
the players inventory.

Ultimately it would probobly be most simple for this class to work closest with the Save_Manager
class so our source code isnt full of attempts at working with files and writing.reading info


'''
class Player(object):
    def __init__(self):
        pass

    def writeToSave(self):
        pass

    #this will likely have to exist in some capacity, however player attributes can likely be
    #simply read from the save when the player object is initialized when the game is launched
    def readFromSave(self):
        pass
    pass





