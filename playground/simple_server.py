import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = 'www.google.com'
host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(99)

while (1):
    c, addr = s.accept()
    print("got connection from {0}".format(addr))
    c.send(b"Thank you for conencting")
    c.close()
