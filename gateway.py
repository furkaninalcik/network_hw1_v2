#!!!	Routing is done by an if-elif pair in the getter functions fromU1 and fromT1



from socket import *
import time
from time import time
import datetime
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore


messageFromT1=""
messageFromU1=""
messageToT2=""
messageToU2=""

totalMessageNofromT1=0
totalMessageNofromU1=0



toU2Flag=0
toT2Flag=0

def fromU1():			#No need to any initialization here
	
	global routingTable
	global messageFromT1
	global messageFromU1
	global messageToT2
	global messageToU2
	global toU2Flag
	global toT2Flag
	global totalMessageNofromT1
	global totalMessageNofromU1

	while 1:
		messageFromU1, U1ClientAddress = serverSocketFromU1.recvfrom(2048)	#U1 client address is actually unnecessary
		#fromU1Lock.acquire()			Deadlock risk
		#!!!Below, routing takes place
		totalMessageNofromU1+=1

		if messageFromU1[-2:]=="U3":	#This one will go to U3 via U2
			toU2Lock.acquire()
			messageToU2=messageFromU1
			toU2Flag=1
			toU2Lock.release()

		elif messageFromU1[-2:]=="T3":	#This one will go to T3 via T2
			toT2Lock.acquire()
			messageToT2=messageFromU1
			toT2Flag=1
			toT2Lock.release()



def fromT1():

	global routingTable
	global messageFromT1
	global messageFromU1
	global messageToT2
	global messageToU2
	global toU2Flag
	global toT2Flag
	global totalMessageNofromT1
	global totalMessageNofromU1

	#serverSocketFromT1.listen(0)									#Start listening for calls from T1
	print "Gateway is listening to T1"
	
	while 1:		
		connectionSocket, T1ClientAddress = serverSocketFromT1.accept()	#Now a connection established			
		messageFromT1=	connectionSocket.recvfrom(2048)
		#fromT1Lock.acquire() 			Deadlock risk
		#!!!Below, routing takes place
		totalMessageNofromT1+=1
		print "TEST A\n"
		print messageFromT1  
		print messageFromT1[0]  

		if messageFromT1[0][-2:]==	"U3": #This one will go to U3 via U2
			toU2Lock.acquire()
			messageToU2=messageFromT1
			print "messageFromT1 is " + messageToU2
			toU2Flag=1
			toU2Lock.release()	
		if messageFromT1[0][-2:]==	"T3": #This one will go to T3 via T32
			print "TEST 1\n"
			toT2Lock.acquire()
			messageToT2 += messageFromT1[0]
			print messageToT2 + "\n"
			toT2Flag=1
			toT2Lock.release()	


def toU2():					#Send the message to U2. This does nothing complicated, just sends

	global routingTable
	global messageFromT1
	global messageFromU1
	global messageToT2
	global messageToU2
	global toU2Flag
	global toT2Flag

	toU2Lock.acquire()
	if toU2Flag==1:
		clientSocketToU2.sendto(messageToU2,(toU2ServerName,toU2ServerPort))
		toU2Flag=0
	toU2Lock.release()


def toT2():					#Send the message to T2. However, must first connect to the TCP server of T2

	global routingTable
	global messageFromT1
	global messageFromU1
	global messageToT2
	global messageToU2
	global toU2Flag
	global toT2Flag
	global toT2ServerName
	global toT2ServerPort

	clientSocketToT2.connect((toT2ServerName,toT2ServerPort))
	while 1:
		toT2Lock.acquire()
		if toT2Flag==1:
			print "sending " + messageToT2 + " to T2"
			clientSocketToT2.send(messageToT2)
			toT2Flag=0
		toT2Lock.release()



fromU1Lock=th.Lock()
fromT1Lock=th.Lock()
toU2Lock=th.Lock()
toT2Lock=th.Lock()

fromU1ServerPort = 10011								#change to -> 10011
serverSocketFromU1=socket(AF_INET, SOCK_DGRAM)
serverSocketFromU1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # This line is to reuse the socket
serverSocketFromU1.bind(("", fromU1ServerPort))			#Bilgehan:Check if listen required

fromT1ServerPort = 10001								#change to -> 10001
serverSocketFromT1=socket(AF_INET,SOCK_STREAM)
serverSocketFromT1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # This line is to reuse the socket
serverSocketFromT1.bind(("",fromT1ServerPort))
serverSocketFromT1.listen(1)							#Start listening for calls from T1 
													#From here, gateway will listen T1. Acceptance of calls is in thread fromT1

toU2ServerName = "U2"								#This is where the data for U2 will be sent
toU2ServerPort = 30002								#change to -> 30002
clientSocketToU2 = socket(AF_INET, SOCK_DGRAM)
clientSocketToU2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # This line is to reuse the socket


toT2ServerName = "131.94.144.29"								#This is where the data for T2 will be sent. Connection is in thread to T2
toT2ServerPort = 20002								#change to -> 20002
clientSocketToT2 = socket(AF_INET, SOCK_STREAM)
clientSocketToT2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # This line is to reuse the socket


U1Acceptor =  th.Thread(target=fromU1,)
T1Acceptor =  th.Thread(target=fromT1,)
U2Sender =  th.Thread(target=toU2,)
T2Sender =  th.Thread(target=toT2,)

U1Acceptor.start()
T1Acceptor.start()
U2Sender.start()
T2Sender.start()

U1Acceptor.join()
T1Acceptor.join()
U2Sender.join()
T2Sender.join()


serverSocketFromT1.close()
serverSocketFromU1.close()
clientSocketToT2.close()
clientSocketToU2.close()


