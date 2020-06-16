import socket
import time

#from listen import awaitREDYFX

# COMMANDS TO SONAR 
FX	= "46581500000000000000000000000000000000b3000000000000000000"
FV	= "46561500000000000000000000000000000000b1000000000000000000"
FC	= "464315002c0100000000000000040000000000cf000a4f0079f5be0000"

# COMMANDS TO PC
BUSY	= "ff00ff000a0042555359"
REDYFX	= "ff00ff00200052454459465816000100303030303030373937360a4f0079f5be"
REDYFC	= "ff00ff0054015245445946434a012c010000900100000000000010001401034a044f0079f5bee8"
#					 15  17  19  21  23  25  27  29
#MINRANGE	= 16
#MAXRANGE	= 18
#DEPTH		= 23
#DEPTH_FRAC	= 25
#TEMPERATURE	= 26
#BATTERY	= 30
#BATTERY_FRAC	= 31
#BUSY	= "42555359"
#REDYFX = "524544594658"
#REDYFC	= "524544594643"

# Opens IPv4 socket, listening for UDP packets
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Converts hex to bytes, Sends UDP message
def sendMessage(msg):
	byte_message = bytes.fromhex(msg)
	opened_socket.sendto(byte_message, ("192.168.1.1", 5000))

# Handshake
def init():
	for i in range(2):
		sendMessage(FX)
		time.sleep(0.12)
		# Send 5 FV messages
		for i in range(5):
			sendMessage(FV)
			time.sleep(0.1)

# Send FC until interrupted
def dataRequest():
	sendMessage(FC)
	time.sleep(0.13)

# Execute program
init()
print ("Connected to SP100. Sending packet requests...")
while 1:
	dataRequest()
