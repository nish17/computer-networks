import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname() # Get local machine name
port = 12345

s.connect(("127.0.0.1", port))
while True:
    buf = input('Enter a message to send: ')
    s.send(buf)
    if buf == 'bye':
        break
    msg = s.recv(1024)
    print 'received ' + msg
    if msg == 'bye':
        break
