#intent is for this to be the script that you run in your terminal to actually play the game


#this is the method that will likely contain the loop which makes the game go
from msilib.schema import File
import string
import World
import Interface
import os
import time
import Player
import Mon
#import sys

def play_game():
    
    
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
    filemon = Mon.Mon(None, None) #temporary filemon instance
    interface = Interface.Interface()
    
    print(interface.startScreen)
    interface.printHud()
    textToAdd = ""

    while(not isFinished):
        #we should somehow clear our terminal sessions output here
        input = Interface.getKeyPress()
        os.system('cls')
        interface.clearLog()
        match interface.mode:
            case 'START':
                
                command = interface.startMenu(input)
                if(command == "NEW"):
                    world.generateWorld(player.position, player)
                if(command == "CONTINUE"):
                    #LOAD FROM SAVE FILE INTO PLAYER
                    world.generateWorld(player.position, player)
                if(command == "STOP"):
                    isFinished = True

            case 'MENU':
                pass
            
            case 'WOLRD':
                
                if(input == 's'):

                    player.position+=1 
                    #world.generateWorld(player.position, player)
                    

                if(input == 'd'):
                    #go into directory at 
                    status = world.moveIntoDir(player)            
                    #world.generateWorld(player.position, player)
                    if(isinstance(status[1], os.stat_result)):
                        #FILEMONCODE HERE
                        
                        textToAdd = ("its a " + status[0])
                        

                        pass
                if(input == 'e'):
                    status = world.interact(player)
                    if isinstance(status, os.DirEntry):
                        textToAdd = (" | its a " + status.name)
                        
                        
                        filemon = Mon.Mon(status.name, status.stat())
                        #print(filemon.name)
                        #print(filemon.rawStats)

                    else:
                        
                        textToAdd = (" | " + status)
                        
                if(input == 'a'):
            
                    world.movePrevDir(player)
                    #world.generateWorld(player.position, player)            
        
                if(input == 'w'):
                    player.position-=1
                    #world.generateWorld(player.position, player)
        
                if(input == 'm'):
                    #MENU
                    pass

                interface.addToLog(player.currentDir)
                interface.addToLog(textToAdd)
                textToAdd = ""
                world.generateWorld(player.position, player)
            
            case 'BATTLE':
                interface.battle(player, filemon, input)
            
            case 'TRADE':
                pass

        interface.printLog()
        interface.printHud()

        time.sleep(.3) #helps prevent unwanted input from holding down keypress
    pass



play_game()
    
