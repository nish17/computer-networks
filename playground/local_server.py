import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = socket.gethostbyname()

s.bind((host, port))
print("socket is binded to port {0}".format(port))
s.listen(5)
print("socket is listening")

while (1):
    c, addr = s.accept()
    print("got connection from {0}".format(addr))
    c.send(b'Thank you connecting')
    c.close()
