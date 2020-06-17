import socket
import time

# Commands to sonar
FX	= "46581500000000000000000000000000000000b3000000000000000000"
FV	= "46561500000000000000000000000000000000b1000000000000000000"
FC	= "464315002c0100000000000000040000000000cf000a4f0079f5be0000"

# Opens IPv4 socket, listening for UDP packets
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Converts hex to bytes, sends UDP message
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
print ("Connected to Sonar. Sending packet requests...")
while 1:
	dataRequest()
