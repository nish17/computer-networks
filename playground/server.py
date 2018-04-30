import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12355

# print(socket.gethostbyname(socket.gethostname))
s.bind((host, port))
print("socket is binded to port {0}".format(port))
s.listen(99)
print("listening to port {0}".format(port))

while (1):
    c, addr = s.accept()
    print("Got connection from {0}".format(addr))
    c.send(b"Thank you connecting..")
    c.close()