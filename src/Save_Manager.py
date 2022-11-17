'''
This will save the player's information: name(?), position, and filemon, as a json object that will be 
stored in a folder called "Saves".

'''
import pickle
#import pandas as pd
import src.Player as Player

def __init__(self):
        
    pass

#Saves player object to pickle file in the saves folder
def saveGame(playerObj):
    with open('GameSaves/save.pkl', "wb") as savefile:
        pickle.dump(playerObj, savefile)
            
    savefile.close()
        
#Loads player object from pickle file and returns player object 
def loadGame():
        
    with open('GameSaves/save.pkl', "rb") as savefile:
        playerObj = pickle.load(savefile)
            
    savefile.close()
    return playerObj  
   






