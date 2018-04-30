import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1217
s.bind((host, port))
s.listen(10)
print("binded at port {0}".format(port))
c, addr = s.accept()
while 1:
    data = c.recv(1024)
    if not data:
        break
    c.sendall(data)

c.close()
