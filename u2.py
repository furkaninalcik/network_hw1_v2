from socket import *
import time
from time import time
import datetime
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore




messageToU3=""
totalMessageNo=0

toU3ServerName = "U3"
toU3ServerPort= 30003
clientSocketToU3 = socket(AF_INET, SOCK_DGRAM)			#This will talk to U3's UDP server, 30003



#Or say for i in 1000
while 1:
	messageFromToU3, U1ClientAddress = serverSocketFromU1.recvfrom(2048)	#U1 client address is actually unnecessary
	messageToGateway=raw_input()
	a=time()
	messageToGateway=messageToGateway + "Seperator" +a + destination			#Time is added to the end of message to compute the time difference
																				#Destination is added to the end so routers know which route to use
																				#Seperator is for easiness in processing at destination
	clientSocketToGateway.sendto(messageToGateway,(toGatewayServerName, toGatewayServerPort))
	totalMessageNo+=1





clientSocketToGateway.close()

