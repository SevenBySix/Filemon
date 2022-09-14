#intent is for this to be the script that you run in your terminal to actually play the game


#this is the method that will likely contain the loop which makes the game go
import World
import Interface
import os
import time
import Player

def play_game(object):
    
    
    '''
    This is where the game will be initialized
    ultimately the player object will be initialized first, and the world will be created
    based on the location of the player
    '''
    
    
    #world.generateWorld(4)
    player = Player.Player('C:/Users', 0) #this should pull data from save as it is initialized
    world = World.World(player.currentDir, player.position)
    world.populateFilenames(player)
    isFinished = False
    world.generateWorld(player.position, player)
    
    inputLock = False
    inputUsed = False

    while(not isFinished):

        input = Interface.getKeyPress()
        
        if(input == 's'):

            player.position+=1 #to be replaced with something that updates the player objects position
            
            world.generateWorld(player.position, player)
        if(input == 'd'):
            #go into directory at 
            world.moveIntoDir(player)            
            world.generateWorld(player.position, player)
            
            pass
        if(input == 'a'):

            pass
        
        if(input == 'w'):
            player.position-=1
            world.generateWorld(player.position, player)
            
        time.sleep(.3) #helps prevent unwanted input from holding down keypress
    pass



play_game(object)
    