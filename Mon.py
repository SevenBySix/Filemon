#This will be the class that will hold a Filemons properties
#the player class will contain some sort of array of FileMon objects
#So when
#An individual mon will ultimately have various text labels and stats attached to it
#in order to do things like trade and battle we will need mon objects to work with
#so that we are not having to constantly modify a mon object in the players inventory
#itll look kinda like making an instance of a mon based on an existing mon of the player
#and later after no changes are happening to that mon, putting that mon instance back where it
#came from, or in the case of trading deleting it and adding the newly recieved mon instance

class Mon(object):
    '''('desktop.ini', 
    os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, 
    st_size=174, st_atime=1664644343, st_mtime=1622894933, st_ctime=1622894933))'''
    def __init__(self, name, fileStats):
        self.name = name
        self.rawStats = fileStats
        

    
