import threading


class RobotThread(threading.Thread):
    def __init__(self,clientAddress,robotSocket, queue, lock):
        threading.Thread.__init__(self)
        self.robotAddress = clientAddress
        self.robotSocket = robotSocket
        self.sendQueue = queue

    def run(self):
        print("Robot connection thread operational")

    
    def main(self):
        if self.messageQueue.empty() is not True:
            sendingMessage = self.messageQueue.get()
            self.robotSocket.sendAll(sendingMessage.bytes())