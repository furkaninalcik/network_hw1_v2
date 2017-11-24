from socket import *
import time
from time import time
import datetime
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore




messageToGateway=""
totalMessageNo=0


toGatewayServerName = "131.94.144.30"
toGatewayServerPort= 10001
clientSocketToGateway = socket(AF_INET, SOCK_STREAM)			#This will talk to gateway's TCP server,10001
clientSocketToGateway.connect( (toGatewayServerName,toGatewayServerPort) )
#	clientSocketToT2.connect((toT2ServerName,toT2ServerPort))



target=raw_input("Who do you want to talk to\n")

if target=="U3":								#The destination is set
	destination="T1U3"
else:
	destination="T1T3"

print "Target: " + target + "Destination: " + destination




#Or say for i in 1000
while 1:

	messageToGateway=raw_input("Write your message: \n")
	a=time()
	messageToGateway=messageToGateway + destination			#Time is added to the end of message to compute the time difference
																				#Destination is added to the end so routers know which route to use
	clientSocketToGateway.send(messageToGateway)
	totalMessageNo+=1







clientSocketToGateway.close()
