import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
# ip = socket.gethostbyname('www.google.com')
# print(ip)
s.bind(('127.0.0.1', port))
print("socket binded to port {0}".format(port))
s.listen(5)
print("socket is listening")

while (1):
    c, addr = s.accept()
    print("Got connection from {0}".format(addr))
    c.send(b'Thank you for connecting')
    c.close()
