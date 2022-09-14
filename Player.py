'''
this class will need to contain player data
a player object will have to include some sort of array or other dataset containing/representing
the players inventory.

Ultimately it would probobly be most simple for this class to work closest with the Save_Manager
class so our source code isnt full of attempts at working with files and writing.reading info


'''


#player will need to hold a vertical location and its path, its name, filemon array

class Player(object):
    
    def __init__(self, directory, pos):
        self.currentDir = directory
        self.position = pos
        

    def writeToSave(self):
        #end state, should look something like Save_manager.write(self)
        pass

    #this will likely have to exist in some capacity, however player attributes can likely be
    #simply read from the save when the player object is initialized when the game is launched
    def readFromSave(self):
        #should look something like Save_manager.read(self)
        #the save manager should then set all necessary player fields to whatever attributes are contained in the save, I think this is the write way to do it
        pass


    pass


