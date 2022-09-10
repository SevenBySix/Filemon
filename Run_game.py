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
    
    inputLock = False
    inputUsed = False

    while(not isFinished):

        input = Interface.getKeyPress()
        
        if(input == 's'):

            playerPosition+=1 #to be replaced with something that updates the player objects position
            world.generateWorld(playerPosition)
                       
        
            
        
        if(input == 'w'):
            playerPosition-=1
            world.generateWorld(playerPosition)
            
        time.sleep(.3) #helps prevent unwanted input from holding down keypress
    pass



play_game(object)
    