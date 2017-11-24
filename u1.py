from socket import *
import time
from time import time
import datetime
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore




messageToGateway=""
totalMessageNo=0

toGatewayServerName = "Gateway"
toGatewayServerPort= 10011
clientSocketToGateway = socket(AF_INET, SOCK_DGRAM)			#This will talk to gateway's UDP server,10011


target=raw_input("Who do you want to talk to\n")

if target=="U3":								#The destination is set
	destination = "U1U3"
else:
	destination = "U1T3"

print "Sending a message to " + target



#Or say for i in 1000
while 1:

	messageToGateway=raw_input("Write your message:\n")
	a=time()
	messageToGateway=messageToGateway + "Seperator" + str(a) + destination			#Time is added to the end of message to compute the time difference
																				#Destination is added to the end so routers know which route to use
																				#Seperator is for easiness in processing at destination
	clientSocketToGateway.sendto(messageToGateway,(toGatewayServerName, toGatewayServerPort))
	totalMessageNo+=1





clientSocketToGateway.close()

