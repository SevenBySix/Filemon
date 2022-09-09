import keyboard


class Interface(object):
    
    #prints a single line of texts to show keybindings
    def printHud(self):
              #remember the game screen is 60 characters long           v60v
              #123456789012345678901234567890123456789012345678901234567890
        print("| up:W  down:S  left:A  right:D  interact:E   menu/quit:ESC|")
        pass

    #prints all information related to the mon in a readable format
    #this will basically be the go to method whenever a mon needs to be represented in game
    def printMon(self):

        pass

    def getKeyPress(self):
        press = keyboard.read_key()
        return press
def getKeyPress():
        press = keyboard.read_key()
        return press






