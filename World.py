import os
    
class World(object):
    #                                                            61 accross
    
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

    def generateWorld(self, characterPosition):
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




