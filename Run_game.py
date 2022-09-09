#intent is for this to be the script that you run in your terminal to actually play the game


#this is the method that will likely contain the loop which makes the game go
import World

def play_game(object):
    startingPath = '''C:/Users'''
    world = World.World(startingPath)
    world.populateFilenames()
    world.generateWorld(4)
    
    pass



play_game(object)
    