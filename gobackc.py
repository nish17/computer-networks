import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12345
s.connect(('',port))
a = int(raw_input('Enter the no of frames '))
b = int(raw_input('Enter the window size '))
x=(a/b)+(a%b)
ack=0
#s.send(str(a))
#s.send(str(b))
#time.sleep(10)
while True:
	for sent in range(ack,ack+b):
		print("sending frame ",sent)
		s.send(str(sent))
		time.sleep(2)
	#s.send("Enter ack number")		
	ack=int(s.recv(1024))
	if ack==a:
		break
	else:
		sent=ack

