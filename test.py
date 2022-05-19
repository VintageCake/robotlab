import queue
import sys
import socket
import threading
import argparse
from ClientThread import ClientThread
from RobotThread import RobotThread

parser = argparse.ArgumentParser()
parser.add_argument("-d", '--destination', required=True, metavar="robot_address", help="Destination address of the robot to connect to")
parser.add_argument("-p", '--port', required=True, metavar="robot_port", help="Port of the robot to connect toDestination port of the robot to connect to", type=int)
args = parser.parse_args()
print(args)

listeningPort = 7000
robotSocket = None
retries = 0

programLock = threading.Lock()
msgQueue = queue.Queue()

for i in range(0,3): # three retries
    try:
        print(f"Connecting to {args.destination}:{args.port}")
        robotSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        robotSocket.connect((args.destination, args.port))
    except socket.error:
        print("Timeout, retrying...")
        retries += 1
        continue
    else:
        break

if retries == 2:
    sys.exit("Wasn't able to complete the connection to the robot, exiting...")
else:
    robotThread = RobotThread(args.destination, robotSocket, queue)
    robotThread.start()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listenSocket:
    try:
        listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listenSocket.bind(("127.0.0.1", listeningPort))
    except socket.error:
        sys.exit(f"Was not able to bind to port {listeningPort}")
    print(f"Listening on port {listeningPort}")

    listenSocket.listen()
    while True:
        print("Testing")
        newClientSocket, newClientAddress = listenSocket.accept()
        newThread = ClientThread(newClientAddress,newClientSocket, msgQueue)
        newThread.start()

