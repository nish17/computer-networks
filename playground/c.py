import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

s.connect((host, port))

while 1:
    d = s.recv(1024)
    if not d:
        break
    s.send(d)
    s.close()
