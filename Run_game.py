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
    startingDir = os.getcwd() + '\\home'
    
    player = Player.Player(startingDir, 0) #this should pull data from save as it is initialized
    world = World.World(player.currentDir, player.position)
    world.populateFilenames(player)
    isFinished = False
    filemon = Mon.Mon('', [0,0,0,0,0,0,0,0,0], '') #temporary filemon instance
    interface = Interface.Interface()
    
    print(interface.startScreen)
    interface.printHud()
    textToAdd = ""
    confirm = False
    skipInput = False
    startingFlag = True

    while(not isFinished):
        #we should somehow clear our terminal sessions output here
        
        if skipInput: 
            skipInput = False
            
        else:
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
                    status = world.interact(player, 1)
                    
                    if (isinstance(status, os.DirEntry)) and (status.path in player.previouslyEncountered):
                        
                        player.position +=2
                    else:
                        player.position+=1
                    
                    #world.generateWorld(player.position, player)
                    

                if(input == 'd'):
                    #go into directory at 
                    status = world.moveIntoDir(player)            
                    #world.generateWorld(player.position, player)
                    if(isinstance(status[1], os.stat_result)):
                        #FILEMONCODE HERE
                        
                        textToAdd = (" | its a " + status[0] + " | press e to interact")
                        

                        pass
                if(input == 'e'):
                    status = world.interact(player, 0)

                    if isinstance(status, os.DirEntry):
                        if(startingFlag and not confirm):
                            
                            textToAdd = (" | its a " + status.name + " | choose this first Filemon?")
                        elif(startingFlag):
                            pass
                        else:
                            textToAdd = (" | its a " + status.name + " | press e again to engage" + ' DEBUG: ' + status.path)
                        
                        
                        filemon = Mon.Mon(status.name, status.stat(), status.path)
                        q = False #basically a simple fix for preventing unwanted action with confirmation action and startingflag
                        if(confirm):
                            #start
                            confirm = False
                                
                            if not startingFlag: skipInput = True

                            if(startingFlag):
                                player.addFilemon(filemon)
                                #interface.setModeWorld()
                                interface.clearLog()
                                startingFlag = False
                                q = True
                                #startingFlag = False
                                skipInput = False
                                #startingFlag = False
                                
                            else:
                                interface.setModeBattle()
                            
                        
                        if not q: confirm = True  
                    else:
                        
                        textToAdd = (" | " + status)
                else:
                    confirm = False
                    

                if(input == 'a'):
            
                    world.movePrevDir(player)
                    #world.generateWorld(player.position, player)            
        
                if(input == 'w'):
                    status = world.interact(player, -1)
                    if (isinstance(status, os.DirEntry) and (status.path in player.previouslyEncountered)):
                        
                        player.position -=2
                    else:
                        player.position-=1
                    #world.generateWorld(player.position, player)
        
                if(input == 'm'):
                    #MENU
                    pass
                
                
                interface.addToLog(player.currentDir)
                interface.addToLog(textToAdd)
                textToAdd = ""
                world.generateWorld(player.position, player)
                status = None
            case 'BATTLE':
                confirm = False
                
                print('battle')
                interface.addToLog(' | type: '+filemon.type)
                filemon.displayMon()
                
                if(interface.battle(player, filemon, input)): #the battle method returns true when battle is completed
                                                       #It will also modify the players filemon and enemy filemon
                                                       #objects appropriately
                    os.system('cls')
                    
                    interface.addToLog(' | Battle Completed')
                    interface.setModeWorld()
                    world.generateWorld(player.position, player)
                    interface.addToLog(' | type: '+filemon.type)
                    
                


                
            case 'TRADE':
                pass

        interface.printLog()
        interface.clearLog()
        textToAdd = ''
        interface.printHud()

        time.sleep(.3) #helps prevent unwanted input from holding down keypress
    pass



play_game()
    
