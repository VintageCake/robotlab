import threading


class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientSocket, queue, lock):
        threading.Thread.__init__(self)
        self.clientSock = clientSocket
        self.clientAdd = clientAddress
        self.messageQueue = queue
    
    def run(self):
        print(f"New client from: {self.clientSock.getpeername()}, thread started")
