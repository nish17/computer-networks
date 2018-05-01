import socket

udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

ipAddress = "127.0.0.1"
port = 12345

while True:
    buf = raw_input('Enter a message to send:')
    udpSocket.sendto(buf, (ipAddress, port))
    if buf == 'bye':
        break

    message = udpSocket.recvfrom(1024)

    print 'Message from Server:' + str(message)
    if message[0] == 'bye':
        break
