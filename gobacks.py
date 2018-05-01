import socket 
import time 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12345 
s.bind(('',port))
s.listen(5)
ac=[]
c,addr=s.accept()
i=0		
a=int(raw_input('enter a'))
b=int(raw_input('enter b'))
while True:
	for i in range(b):	
		f=c.recv(256)
		print("Frame received ",f)
		time.sleep(2)
	ack=raw_input('Enter acknowledgement')
	c.send(str(ack))	
	if ack==a:
		break

