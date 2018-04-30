import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12355
s.connect((host, port))
while (1):
    print(s.recv(1024))
    s.close()
