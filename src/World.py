import os
import src.Player

class World(object):
    #                                                            61 accross
    #this just helps visualize what the screen looks like
    screen = '''
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    |                                                            |
    '''

    
    def __init__(self, startingPosition, verticalLoc):
        self.currentPosition = startingPosition #this is a string of the current path
        self.verticalLoc = verticalLoc #this is the number corresponding to the file the player is on
        self.filenames = []
        

    def populateFilenames(self, player):
        self.filenames = []
        for file in os.scandir(player.currentDir):
            self.filenames.append((file.name, file.path))
        #print(self.filenames)
        pass


    def clearScreen(self):#this should clear the screen, however it does not work
        if os.name == 'nt':
             
             os.system('cls')
        else:
             os.system('clear')
    
    def checkNext(self, player, direction):
        pass


    def moveIntoDir(self, player):
        iterator = 0
        #print(player.currentDir)
        #print(player.position)
        for file in os.scandir(player.currentDir):
            if iterator == player.position:
                if file.is_dir():
                    #print(file.is_dir())
                    #print('its a dir')
                
                
                    
                        
                        
                    try:
                        os.scandir(file.path)
                    except:
                        #print('NO ACCESS')
                        return ('NO_ACCESS')
                        
                            
                    player.currentDir = file.path
                    #print("currentPosition updated")
                    #print(player.currentDir)
                    self.populateFilenames(player)
                    player.position = 0
                    return player.currentDir                    
                else:
                    #print('Filemon')
                    #print(file.stat())
                    return (file.name, file.stat())
            iterator+=1
    #returns the current file, if its a dir does not go inside
    def interact(self, player, posFromPlayer):
        targPos = player.position + posFromPlayer
        iterator = 0
        for file in os.scandir(player.currentDir):
            if iterator == targPos:
                if file.is_dir():
                    try:
                        os.scandir(file.path)
                        return ('this goes to '+file.path)
                    except:
                        
                        return ('Its blocked off')
                    
                                        
                else:
                    
                    return file
            iterator+=1
        
    #example path: C:\Program Files\ASUS\Aac_Mouse
    def movePrevDir(self, player):
        player.currentDir = os.path.dirname(player.currentDir)
        self.populateFilenames(player)
        return player.currentDir

    def generateWorld(self, characterPosition, player):
        partialLine= ''
        self.populateFilenames(player)
        
        character = "@"
        
        finishedWorld = ''
        position = 0
        for filename in self.filenames:
            if filename[1] in player.previouslyEncountered:
                pass
                
            elif position == characterPosition:
                
                partialLine = '|       ' + character + ' ' + filename[0]
            else:
                
                partialLine = '|         ' +  filename[0]

            for i in range(len(partialLine), 60):
                partialLine += ' '
            partialLine += '|\n'
            finishedWorld += partialLine
            position+=1
            partialLine = ''
        finishedWorld = finishedWorld[:len(finishedWorld)-1]
        print(finishedWorld)
        

    def clearScreen(object):
        pass




