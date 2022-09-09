#intent is for this to be the script that you run in your terminal to actually play the game


#this is the method that will likely contain the loop which makes the game go
import World
import Interface
import os
import time


def play_game(object):
    startingPath = '''C:/Users'''
    
    '''
    This is where the game will be initialized
    ultimately the player object will be initialized first, and the world will be created
    based on the location of the player
    '''
    world = World.World(startingPath)
    world.populateFilenames()
    #world.generateWorld(4)
    playerPosition = 0
    isFinished = False
    world.generateWorld(playerPosition)
    while(not isFinished):
        
        if(Interface.getKeyPress() == 's'):
            playerPosition+=1 #to be replaced with something that alters position in save_manager
            world.generateWorld(playerPosition)
            
        if(Interface.getKeyPress() == 'w'):
            playerPosition-=1
            world.generateWorld(playerPosition)
            
        time.sleep(1)
    pass



play_game(object)
    