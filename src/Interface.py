from email.errors import FirstHeaderLineIsContinuationDefect
from tokenize import String
import keyboard
import random
from src import network

class MODES:
    START = "START"
    MENU = "MENU"
    WORLD = "WOLRD"
    BATTLE = "BATTLE"
    TRADE = "TRADE"


class Interface(object):

    #prints a single line of texts to show keybindings


    def __init__(self):
        self.mode = MODES.START
        self.menuPosition = 322 #number of chars in the first menu items starts at
        self.startScreen = '''
                                                              
                    █〓 █ ▙▄ █☰ ▛▚▞▜ ██ ▛▟                    
|                                                           | 
|                                                           | 
|                                                           | 
|     >NEW GAME                                             | 
|      CONTINUE                                             | 
|      EXIT                                                 | 
|                                                           |
|                                                           |'''
        self.log = ''
        
        self.battlePosition = 1
        self.battleLog = ''
        self.firstGo = True #so that we can print battle or trade screens
                            #before we collect user input
        self.inventoryPosition = 0 #position of 0 represents inventory not being open
        
        self.menuArea = 'menu'

        self.tradePosition = [0, 9]
        self.priorInput = ''
        self.tradeReady = False
        self.otherMon = None

    def printHud(self):
              #remember the game screen is 60 characters long           v60v
              #123456789012345678901234567890123456789012345678901234567890
        print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC |")
        pass

    def addToLog(self, new):
        
        self.log += new
        pass

    def clearLog(self):
        self.log = '|'
        pass

    def printLog(self):
        
        print(self.log + (60-len(self.log))*' '+'|')
        
    def setModeStart(self):
        self.mode = MODES.START

    def setModeMenu(self):
        self.mode = MODES.MENU
        self.menuPosition = 7
        self.firstGo = True

    def setModeWorld(self):
        self.mode = MODES.WORLD

    def setModeBattle(self):
        self.mode = MODES.BATTLE
        self.menuPosition = 63#update this

    def setModeTrade(self):
        self.mode = MODES.TRADE
        self.firstGo = True
   
    def startMenu(self, input):

        constant = 63 #number of chars in the next menu item is
        
        screen = '''
                                                              
                    █〓 █ ▙▄ █☰ ▛▚▞▜ ██ ▛▟                     
|                                                           | 
|                                                           | 
|                                                           | 
|      NEW GAME                                             | 
|      CONTINUE                                             | 
|      EXIT                                                 | 
|                                                           | '''
#7
        screenChars = list(screen)
        
        match input:
            case 'w':
                screenChars[self.menuPosition] = ' '
                self.menuPosition-=constant
                screenChars[self.menuPosition] = '>'
                print(''.join(screenChars))
            case 's':
                screenChars[self.menuPosition] = ' '
                self.menuPosition+=constant
                screenChars[self.menuPosition] = '>'
                print(''.join(screenChars))
            case 'e':
                if(screenChars[self.menuPosition+1] == "N"):
                    self.setModeWorld()
                    return "NEW"
                if(screenChars[self.menuPosition+1] == "C"):
                    self.setModeWorld()
                    #player populated in Run_game, not in here
                    
                    return "CONTINUE"
                if(screenChars[self.menuPosition+1] == "E"):

                    return "STOP"
    
    def menu(self, player, input):
        # CONTINUE EXIT SAVE TRADE
        constant = 63
        menuScreen = '''
|      CONTINUE                                              |
|      SAVE                                                  |
|      FILEMONS                                              |
|      ITEMS                                                 |
|      TRADE                                                 |
|      EXIT                                                  |
|                                                            |
|                                                            |
|                                                            |'''
        screenChars = list(menuScreen)
        if self.firstGo:
            screenChars[7] = '>'
            print(''.join(screenChars))
            self.firstGo = False
        else:
            match input:
                case 'w':
                    screenChars[self.menuPosition] = ' '
                    self.menuPosition-=constant
                    screenChars[self.menuPosition] = '>'
                    print(''.join(screenChars))
                case 's':
                    screenChars[self.menuPosition] = ' '
                    self.menuPosition+=constant
                    screenChars[self.menuPosition] = '>'
                    print(''.join(screenChars))
                case 'e':
                    if(screenChars[self.menuPosition+1] == "C"):
                        return 'CONTINUE'
                    if(screenChars[self.menuPosition+1] == "S"):
                        #saving handled in Run_game
                        print(''.join(screenChars))
                        return 'SAVE'
                    if(screenChars[self.menuPosition+1] == "F"):
                        #LIST FILEMON AND STATS
                        monList = ''
                        for mon in player.filemons:
                            monStats = '(hp: ' + str(mon.hp) + '/' + str(mon.stats[0]) + 'Atk: '+str(mon.stats[1]) + ')'

                            monList += '|    [    ' + mon.name + (25 - len(mon.name))*' ' + monStats  + (20 - len(monStats))*' ' + ']    |' + '\n'
                        print(monList)
                        return "FILEMON_LIST"
                    if(screenChars[self.menuPosition+1] == "I"):
                        itemList = ''
                        for item in player.inventory:
                            itemList += '|    [    ' + item + (45 - len(item))*' ' + ']    |' + '\n'
                        print(itemList)
                        return "ITEMS"
                    if(screenChars[self.menuPosition+1] == "T"):
                    
                        return "TRADE"
                    
                    if(screenChars[self.menuPosition+1] == "E"):

                        return "EXIT"

    def trade(self, player, input):
        monList = ''
        statusLine = ''
        constant = 62
        

        for mon in player.filemons:
            monStats = '(hp: ' + str(mon.hp) + '/' + str(mon.stats[0]) + 'Atk: '+str(mon.stats[1]) + ')'

            monList += '|    [    ' + mon.name + (25 - len(mon.name))*' ' + monStats  + (20 - len(monStats))*' ' + ']    |' + '\n'
        monList = list(monList)
        monList[self.tradePosition[1]] = ' '
        if self.firstGo:
            
            self.tradeReady = False
            self.firstGo = False
            self.otherMon = None

        elif input == 'w':
            self.tradePosition[0] -= 1
            self.tradePosition[1] -= constant
        elif input == 's':
            self.tradePosition[0] += 1
            self.tradePosition[1] += constant
        elif input == 'e':
            
            if self.priorInput == 'e' and self.TradeReady:
                #execute trade
                player.filemon[self.tradePosition[0]] = self.otherMon
                return (True, 'Trade completed, recieved: ' )
            else:
                network.sendFilemon(player.filemons[self.tradePosition[0]])
                self.addToLog('press E again to confirm trade')

        self.otherMon = network.recieveFilemon()

        self.priorInput = input
        monList[self.tradePosition[1]] = '>'

        monList = ''.join(monList)
        print(monList)
        try:
            print('the other player wants to send you: ' + self.otherMon.name)
            self.TradeReady = True
        except:
            print('standby for other players trade selection')

        return False, ''


        

    def battle(self, player, filemon, input):
        #This function will be called upon interacting with a wild(or rather unowned) filemon
        screen = '''
|                                                            |
|    [playerMon         ]            [enemyMon          ]    |
|    (==================)            (==================)    |
|                                                            |
|                                                            |
|                                                            |
|   >Fight  Inventory                                        |
|    Info   Flee                                             |
|    [    Battle Log                                    ]    |'''
        #sys.stdout.write("test")
        #sys.stdout.flush()
        firstLine = '''|                                                           |'''
        firstMon = player.filemons[0] #the filemon used will always be the players first filemon
                                      #if we need to switch filemon we are going to swap the position of filemon
                                      #in the characters inventory
        playerMonName = firstMon.name
        enemyName = filemon.name

        inventory = player.inventory + player.filemons #battle uses a combined player and filemon inventory

        if(len(playerMonName) > 19):
            ext = '.' + firstMon.type
            playerMonName = playerMonName[:(len(playerMonName) - len(ext))] + ext
        if(len(enemyName) > 19):
            ext = '.' + filemon.type
            enemyName = enemyName[:len(playerMonName) - len(ext)] + ext
        


        sumChars = len(playerMonName) + len(enemyName) + 4
        numSpaces = 50 - sumChars
        nameLine = '|    ' + '[' + playerMonName + ']' + (' ' * numSpaces) + ' '  + '[' +enemyName + ']' + '    |'
        print(firstLine)
        print(nameLine)
        #int((player.hp/player.stats[0]) * 18) getting number of equal signs to represent hpq
        # 
        #18 chars

        ''' for reference
|                                                            |
|    [playerMon         ]            [enemyMon          ]    |
|    (==================)            (==================)    |
|                                                            |
|                                                            |
|                                                            |
|   >Fight1 Inventory2                                       |
|    Info3  Flee4                                            |
|    [    Battle Log                                    ]    |'''
    
        if not self.firstGo:
            positionItem = []
            i = 1
            #building a usable list of players inventory and filemon
            for item in player.inventory:
                positionItem.append((i, item))
                i += 1
            for item in player.filemons:
                positionItem.append((i, item.name))
                i += 1

            if input == 'e':
                
                
                if self.inventoryPosition == 0:
                    

                    #we dont want to do battle menu things if the inventory is open
                    if self.battlePosition == 1:

                        filemon.hp-=player.filemons[0].stats[1]
                        player.filemons[0].hp -= filemon.stats[1]
                        if player.filemons[0].hp <= 0:
                            
                            player.filemons[0].hp = player.filemons[0].stats[0] #this will ultimately need to be changed to something that swaps the fainted mon to the next mon
                            self.firstGo = True
                            return (True, 'You where defeated')

                        if filemon.hp <= 0:
                            filemon.hp = 0
                            self.firstGo = True
                            player.addDefeated(filemon)
                            return (True, 'You defeated '+filemon.name)

                        self.battleLog = 'attacked for '+str(player.filemons[0].stats[1])+ ' damage'
                    if self.battlePosition == 2:
                        self.inventoryPosition = 1
                    if self.battlePosition == 3:
                        pass
                    if self.battlePosition == 4:
                        if random.randrange(0, 100) > 70:
                            self.firstGo = True
                            return (True, 'you fled')
                else:
                    #inventory position is not zer, so inventory events must occur instead
                    #self.inventory = ['0', 'Capture_Device', 'Healing_Device', 'Throwable_Rock', 'Camera', 'mon1', 'mon2']
                    if positionItem[self.inventoryPosition][1] == 'Capture_Device':
                        missingHp = filemon.stats[0] - filemon.hp

                        percentCapture = float(missingHp)/float(filemon.stats[0])
                        if(random.random() < percentCapture):
                            #player.filemons.append(filemon)
                            player.addFilemon(filemon)
                            self.battleLog = ''
                            return (True, 'Suceesfully Captured '+filemon.name)
                        else:
                            self.battleLog = 'Capture Device activated: Unsuccesful'
                    elif positionItem[self.inventoryPosition][1] == 'Healing_Device':
                        hpToHeal = .25 * player.filemons[0].stats[0]
                        player.filemons[0].hp += hpToHeal
                        if player.filemons[0].hp > player.filemons[0].stats[0]:
                            player.filemons[0].hp = player.filemons[0].stats[0]
                        self.battleLog = 'healed for: ' + str(hpToHeal)
                    elif positionItem[self.inventoryPosition][1] == 'Throwable_Rock':
                        if filemon.hp > 5:
                            filemon.hp-=5
                        self.battleLog = 'That was mean!'
                    elif positionItem[self.inventoryPosition][1] == 'Camera':
                        with open('misc/images.txt', 'a') as f:
                            f.writelines(nameLine+'\n')
                        self.battleLog = 'images saved to: misc/images.txt'
                    else:
                        monIndex = self.inventoryPosition - len(player.inventory)
                        temp = player.filemons[0]
                        player.filemons[0] = player.filemons[monIndex]
                        player.filemons[monIndex] = temp
                    #other item implementation goes here

            '''
            |   >Fight1 Inventory2                                       |
            |    Info3  Flee4                                            |'''
            if input == 'w':
                #battleposition
                if self.battlePosition == 3:
                    self.battlePosition = 1
                if self.battlePosition == 4:
                    self.battlePosition = 2
                
            if input == 's':
                if self.battlePosition == 1:
                    self.battlePosition = 3
                if self.battlePosition == 2:
                    self.battlePosition = 4
            if input == 'a':
                if self.inventoryPosition != 0:
                    self.inventoryPosition -=1
                else:
                    if self.battlePosition == 2:
                        self.battlePosition = 1
                    if self.battlePosition == 4:
                        self.battlePosition = 3
            if input == 'd':
                if self.inventoryPosition != 0:
                    self.inventoryPosition +=1 #scrolling all the way to the left of the inventory
                                          #will have the effect of exiting the inventory
                else:
                    if self.battlePosition == 1:
                        self.battlePosition = 2
                    if self.battlePosition == 3:
                        self.battlePosition = 4
        else:
            self.firstGo = False

        numEquals = int((player.filemons[0].hp/player.filemons[0].stats[0]) * 18)
        numSpaces = 18-numEquals
        numEqualsEn = int((filemon.hp/filemon.stats[0]) * 18)
        numSpacesEn = 18-numEqualsEn


        print('|    ('+ (numEquals*'=')+(numSpaces*' ') +')           ('+
              (numEqualsEn*'=') + (numSpacesEn*' ') + ')    |')
        numEquals = 0
        numEqualsEn = 0
        print(firstLine)
        print(firstLine)
        
        cursorPosition = 7
        if self.inventoryPosition == 0:
            match self.battlePosition:
                case 1:
                    cursorPosition = 4
                case 2:
                    cursorPosition = 11
                case 3:
                    cursorPosition = 66
                case 4:
                    cursorPosition = 73

            battleLines = '''|    Fight1 Inventory2                                      |
|    Info3  Flee4                                           |'''
            battleLines = list(battleLines)
            battleLines[cursorPosition] = '>'
            battleLines = ''.join(battleLines)

            print(battleLines)

            print('|    [    '+self.battleLog+ (((45 - len(self.battleLog))*' '))+']    |')
            self.battleLog = ''
        elif self.inventoryPosition >= 1:
            invLine = ''
            
            
            
            invLine = positionItem[self.inventoryPosition][1] + ' '*(50 -len(positionItem[self.inventoryPosition][1])) 
                    
                        
                

            invLine += '     |'
            print('|    '+invLine)
            print('|    [    '+self.battleLog+ (((45 - len(self.battleLog))*' '))+']    |')
                
            
        #print('\ndebug '+ input + ' '+ str(self.inventoryPosition) + ' '+ str(self.battlePosition)+ '  \n')
        return (False, 'battle engaged') #when finished return true
        

    #prints all information related to the mon in a readable format
    #this will basically be the go to method whenever a mon needs to be represented in game
    def printMon(self):

        pass


    def getKeyPress(self):
            press = keyboard.read_key()
            return press

    def printHud(self):
                  #remember the game screen is 60 characters long           v60v
                  #123456789012345678901234567890123456789012345678901234567890
            print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC |")
            pass


def getKeyPress():
    press = keyboard.read_key()
    return press

def printHud():
          #remember the game screen is 60 characters long           v60v
          #123456789012345678901234567890123456789012345678901234567890
    print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC |")




