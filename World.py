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

    def generateWorld(self):
        print(self.filenames)
        pass

    def clearScreen(object):
        pass




