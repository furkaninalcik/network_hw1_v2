from socket import *
import time
from time import time
import datetime
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore




#messageToT3=""
totalMessageNo=0




fromT2ServerName = "t2"
fromT2ServerPort = 20003


serverSocketFromT2 = socket(AF_INET, SOCK_STREAM)			#This will recieve message from T2s's TCP client, 20003
serverSocketFromT2.bind(("",fromT2ServerPort))
serverSocketFromT2.listen(1)
print "T3 is listening to T2\n"

#clientSocketToT3 = socket(AF_INET, SOCK_STREAM)			#This will talk to U3's UDP server, 30003
#clientSocketToT3.connect((toT3ServerName,toT3ServerPort))


#Or say for i in 1000
while 1:

	connectionSocket, addr = serverSocketFromT2.accept()
	message = connectionSocket.recv(1024)
	print "recieving test"
	#capitalizedSentence = sentence.upper()
	#connectionSocket.send(capitalizedSentence)
	print message															#Destination is added to the end so routers know which route to use
	
	connectionSocket.close()



	'''
	messageFromT2, T1ClientAddress = serverSocketFromT2.recvfrom(2048)	#T1 client address is actually unnecessary
	message=messageFromT2
	a=time()
	#messageToT3 = messageToGateway + "Seperator" +a + destination			#Time is added to the end of message to compute the time difference
	print message															#Destination is added to the end so routers know which route to use
																				#Seperator is for easiness in processing at destination
	#clientSocketToT3.sendto(messageToT3,(toT3ServerName, toT3ServerPort))
	totalMessageNo+=1
'''

#clientSocketToGateway.close()

