'''
This will save the player's information: name(?), position, and filemon, as a json object that will be 
stored in a folder called "Saves".

'''
import json

class Save_Manager():

    def __init__(self):

        pass

    '''Saves player infromation as a json object in the saves folder'''
    def saveGame(currentDir, pos, filemons):
        playerInfo = {
            "currentDir": currentDir,
            "position": pos,
            "filemon": filemons
        }
        
        json_save = json.dumps(playerInfo, indent=4)
        with open("GameSaves/save.json", "w") as outfile:
            outfile.write(json_save)
  
    def loadGame():
        
        pass
   






