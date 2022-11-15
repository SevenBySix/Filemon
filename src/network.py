import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.200"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)
        
    #this is what I will call from Interface to tell your network code to start
    def startNet(self):
        #start thread
        pass

    #this needs to send a filemon object
    def sendFilemon(self, filemon):

        pass

    #I need to be able to call this and get a filemon
    def recieveFilemon(self):
        return None
    
    def stopNet(self):
        #stop thread
        pass