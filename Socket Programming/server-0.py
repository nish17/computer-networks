import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.bind(('', port))

s.listen(5)

while True:
    c, addr = s.accept()

    print 'Got connection from', addr
    c.send('Thank you for connecting\n')

    c.close()
