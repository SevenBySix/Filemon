import os

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

    
    def __init__(self, startingPosition):
        self.currentPosition = startingPosition
        self.filenames = []
        

    def populateFilenames(self):
        print(self.currentPosition)
        for filename in os.listdir(self.currentPosition):
            self.filenames.append(filename)
        pass

    def clearScreen():#this should clear the screen, however it does not work
        if os.name == 'nt':
             
             os.system('cls')
        else:
             os.system('clear')
             
        
        

    def generateWorld(self, characterPosition):
        clear = "\n" * 100 #This is a really ghetto workaround for clearScreen() not working
                           #The purpose of having a clear screen is to make the world look good
        print(clear)

        print(self.filenames)
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




