import os
import Player

class World(object):
    #                                                            61 accross
    #this just helps visualize what the screen looks like
    world = '''
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
            self.filenames.append(file.name)
        print(self.filenames)
        pass


    def clearScreen(self):#this should clear the screen, however it does not work
        if os.name == 'nt':
             
             os.system('cls')
        else:
             os.system('clear')
             
    def moveIntoDir(self, player):
        iterator = 0
        print(player.currentDir)
        print(player.position)
        for file in os.scandir(player.currentDir):
            if file.is_dir:
                print('its a dir')
                if iterator == player.position:
                    player.currentDir = file.path
                    print("currentPosition updated")
                    print(player.currentDir)
                    self.populateFilenames(player)
                    player.position = 0
                    return player.currentDir
            iterator+=1
        
        

    def generateWorld(self, characterPosition, player):
        clear = "\n" * 10 #This is a really ghetto workaround for clearScreen() not working
                           #The purpose of having a clear screen is to make the world look good

        print(clear)
        self.populateFilenames(player)
        
        character = "@"
        worldSize = len(self.filenames)
        finishedWorld = ''
        position = 0
        for filename in self.filenames:
            if position == characterPosition:
                partialLine = '|       ' + character + ' ' + filename
            else:
                partialLine = '|         ' +  filename

            for i in range(len(partialLine), 60):
                partialLine += ' '
            partialLine += '|\n'
            finishedWorld += partialLine
            position+=1


        print(finishedWorld)
        pass

    def clearScreen(object):
        pass




