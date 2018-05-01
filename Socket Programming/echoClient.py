import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

s.connect(("127.0.0.1", port))

buf = raw_input('Enter a message to send: ')
s.send(buf)
print s.recv(1024)
