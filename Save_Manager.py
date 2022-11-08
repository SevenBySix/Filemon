'''
This will save the player's information: name(?), position, and filemon, as a json object that will be 
stored in a folder called "Saves".

'''
import pickle
#import pandas as pd
class Save_Manager(object):
    
    def __init__(self):
        
        pass

    #Saves player object as a json object in the saves folder
    def saveGame(playerObj):
        with open('GameSaves/save.pkl', "wb") as savefile:
            pickle.dump(playerObj, savefile)
        savefile.close()
    #Loads json object from save file and returns player object
    def loadGame():
        
        with open('GameSaves/save.pkl', "rb") as savefile:
            playerObj = pickle.load(savefile)
        savefile.close()
        return playerObj  
   






