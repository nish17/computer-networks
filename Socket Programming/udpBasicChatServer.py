import socket

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udpSocket.bind(('', 12345))

print("UDP server up and listening")

while (True):
    message = udpSocket.recvfrom(1024)
    print "received message from client:" + str(message)

    clientMessage = message[0]
    clientAddress = message[1]

    if clientMessage == 'bye':
        continue

    buf = raw_input("Enter a message for client:")
    udpSocket.sendto(buf, clientAddress)
