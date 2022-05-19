import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", required=True, metavar="robot_address", help="Destination address of the robot to connect to")
parser.add_argument("-p", required=True, metavar="robot_port", help="Port of the robot to connect toDestination port of the robot to connect to", type=int)
args = parser.parse_args()
print(args)