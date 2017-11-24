from socket import *
import time
import threading as th
from multiprocessing import Process, Lock,RLock, Semaphore




print "Hello from U3"


def fromU2():
	global fromU2Flag

	global messageFromU2
	global messageFromU2Reserve	
	print 	"The server for U2 is ready to receive"
	while 1:
		messageFromU2, U2ClientAddress = fromU2serverSocket.recvfrom(2048)
		fromU2Lock.acquire()
		messageFromU2Reserve = messageFromU2
		print "Message from U2 is" + messageFromU2
		fromU2Flag=1
		fromU2Lock.release()


def toU2():
	global fromU2Flag

	global messageFromU2
	global messageFromU2Reserve
	print 	"The client for U2 is ready to receive"
	messageU2Reserve2="Hello from U3"
	clientSocketToU2.sendto(messageU2Reserve2,(toU2ServerName, toU2ServerPort))

	while 1:
		fromU2Lock.acquire()
		if fromU2Flag==1:
			messageU2Reserve2=raw_input("Tell something")
			clientSocketToU2.sendto(messageU2Reserve2,(toU2ServerName, toU2ServerPort))
			print "I tell" + messageFromU2Reserve
			fromU2Flag=0
		fromU2Lock.release()
		



print "Hello from U3 2"

messageFromU2=""
messageFromU2Reserve=""			#Just a precaution

fromU2Flag=0 			# Threads will use this to send messages to each other
fromU2Lock=th.Lock()


print "Hello from U3 3 "

toU2ServerName = "node-0"
toU2ServerPort= 30022
clientSocketToU2 = socket(AF_INET, SOCK_DGRAM)			#Client will talk to U2's 2. server


fromU2ServerPort=30003
fromU2serverSocket = socket(AF_INET, SOCK_DGRAM)
fromU2serverSocket.bind(("", fromU2ServerPort))			#Server is set. It will listen to U2


print "Hello from U3 4"
U2Acceptor =  th.Thread(target=fromU2)		#Start seperate threads. One listens from U2, one sends to U2
U2Sender =  th.Thread(target=toU2)

U2Acceptor.start()
U2Sender.start()

U2Acceptor.join()
U2Sender.join()
print "Hello from U3 5"

fromU2serverSocket.close()