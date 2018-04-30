import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12355

s.bind((host, port))
s.listen(5)
c, addr = s.accept()
print("got connected to {0}".format(addr))
while (1):
    data = c.recv(1024)
    if not data: break
    c.sendall(data)

c.close()