import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12355

s.connect((host, port))
x = str(input("enter data to send:"))
x = str.encode(x)
s.sendall(x)
data = s.recv(1024)
s.close()
print("Received, " + str(data))
