import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 1234

s.bind((host, port))
s.listen(11)

while (1):
    c, addr = s.accept()
    print("Got connection from {0}".format(addr))
    c.send(b"Thank you for connecting")
    c.close()
