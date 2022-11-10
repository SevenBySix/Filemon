#intent is for this to be the script that you run in your terminal to actually play the game


#this is the method that will likely contain the loop which makes the game go
#from msilib.schema import File

import string
from Save_Manager import Save_Manager
import World
import Interface
import os
import time
import Player
import Mon
from sys import platform
#import sys

def play_game():
    
    
    '''
    This is where the game will be initialized
    ultimately the player object will be initialized first, and the world will be created
    based on the location of the player
    '''
    
    
    #world.generateWorld(4)
    if platform == 'linux':
        startingDir = os.getcwd() + '/home'
    else:
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
        if platform == 'linux':
            os.system('clear')
        else:
            os.system('cls')
        interface.clearLog()
        match interface.mode:
            case 'START':
                
                command = interface.startMenu(input)
                if(command == "NEW"):
                    world.generateWorld(player.position, player)
                if(command == "CONTINUE"):
                    player = player.readFromSave()
                    interface.addToLog('game loaded')
                    world.generateWorld(player.position, player)
                if(command == "STOP"):
                    isFinished = True

            case 'MENU':
                command = interface.menu(player, input)
                if command == 'CONTINUE':
                    interface.setModeWorld()
                    skipInput = True
                elif command == 'EXIT':
                    isFinished = True
                elif command == 'SAVE':
                    player.writeToSave()
                    interface.addToLog('Game Saved')
                    #skipInput = True
                elif command == 'TRADE':
                    interface.setModeTrade()
                    skipInput = True
            
            case 'WOLRD':
                if(input == 'o'):
                    isFinished = True

                if(input == 's'):
                    player.position+=1
                    status = world.interact(player, 0)
                    
                    if (isinstance(status, os.DirEntry)) and (status.path in player.previouslyEncountered):
                        #pass
                        interface.addToLog('ran')
                        player.position +=1
                    
                    
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
                        print('DEBUG'+str(filemon.stats[0])+ ' ' + str(filemon.rawStats[6])+ ' '+ str(filemon.stats[1]))
                        
                        if not q: confirm = True  
                    else:
                        
                        textToAdd = (" | " + status)
                else:
                    confirm = False
                    

                if(input == 'a'):
            
                    world.movePrevDir(player)
                    #world.generateWorld(player.position, player)            
        
                if(input == 'w'):
                    player.position-=1
                    status = world.interact(player, 0)
                    
                    if (isinstance(status, os.DirEntry)) and (status.path in player.previouslyEncountered):
                        interface.addToLog('ran')
                        player.position -=1
        
                if(input == 'm'):
                    interface.setModeMenu()
                    skipInput = True
                
                
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
                #interface.battle will now return a tuple in the form of (True/False, 'status')
                battleTuple = interface.battle(player, filemon, input)
                if(battleTuple[0]): #the battle method returns true when battle is completed
                                                       #It will also modify the players filemon and enemy filemon
                                                       #objects appropriately
                    if platform == 'linux':
                        os.system('clear')
                    else:
                        os.system('cls')
                    
                    interface.addToLog(' | Battle Completed, '+ battleTuple[1])
                    interface.setModeWorld()
                    world.generateWorld(player.position, player)
                    interface.addToLog(' | type: '+filemon.type)
                    
                


                
            case 'TRADE':
                done, log = interface.trade(player, input)
                
                if done:
                    #this should eventually be altered such that the player chooses when they want to stop trading
                    interface.addToLog(log)
                    interface.setModeWorld()
                    world.generateWorld(player.position, player)


        interface.printLog()
        interface.clearLog()
        textToAdd = ''
        interface.printHud()

        time.sleep(.3) #helps prevent unwanted input from holding down keypress
    pass



play_game()
    
