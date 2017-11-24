from socket import *
import time
from time import time
import datetime
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore




messageToT3=""
totalMessageNo=0




fromGatewayServerName = "gateway"
fromGatewayServerPort = 20002


serverSocketFromGateway = socket(AF_INET, SOCK_STREAM)			#This will recieve message from gateways's TCP client, 20002
serverSocketFromGateway.bind(("",fromGatewayServerPort))
serverSocketFromGateway.listen(1)
print "T2 is listening to Gateway\n"

toT3ServerName = "131.94.144.28"
toT3ServerPort= 20003
clientSocketToT3 = socket(AF_INET, SOCK_STREAM)			#This will talk to U3's UDP server, 30003
clientSocketToT3.connect((toT3ServerName,toT3ServerPort))


#Or say for i in 1000
while 1:
	
	connectionSocket, addr = serverSocketFromGateway.accept()
	messageFromGateway = connectionSocket.recv(1024)
	print messageFromGateway															#Destination is added to the end so routers know which route to use

	a=time()
	messageToT3 = messageFromGateway 											#Time is added to the end of message to compute the time difference
																				#Destination is added to the end so routers know which route to use
																				#Seperator is for easiness in processing at destination
	clientSocketToT3.send(messageToT3)
	totalMessageNo+=1


clientSocketToGateway.close()

