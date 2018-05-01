import socket   
            
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         

port = 12345                


s.bind(('', port))    
    
Now wait for client connection.
s.listen(5)                 

while True:
	
	c, addr = s.accept()     
	
	print 'Got connection from', addr
	buf=c.recv(1024)
	print 'received ' + buf + '\n'
	print 'echoing it back\n'
	c.send(buf)
	c.close()


