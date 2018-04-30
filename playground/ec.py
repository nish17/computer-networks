import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1217

s.connect((host, port))
s.sendall(b"hello, world")
data = s.recv(1024)

s.close()
print("Received: ", repr(data))
