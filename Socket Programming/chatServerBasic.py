import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    while True:
        buf = c.recv(1024)
        print 'received ' + buf + '\n'
        if buf == 'bye':
            break

        msg = raw_input("Enter a msg")
        c.send(msg)
        if msg == 'bye':
            break
    c.close()
