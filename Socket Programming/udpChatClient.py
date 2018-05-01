import socket
import select
import sys

udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

ipAddress = "127.0.0.1"
port = 12345

while True:
    inputStream_list = [sys.stdin, udpSocket]
    read_sockets, write_socket, error_socket = select.select(
        inputStream_list, [], [])
    for socks in read_sockets:
        if socks == udpSocket:
            message = udpSocket.recvfrom(1024)
            print "<received>" + str(message)
            if message[0] == 'bye':
                udpSocket.close()
                inputStream_list.remove(udpSocket)
                break
        else:
            buf = raw_input()
            udpSocket.sendto(buf, (ipAddress, port))
            print "<You>" + buf
            if buf == 'bye':
                udpSocket.close()
                inputStream_list.remove(udpSocket)
                break
    if udpSocket not in inputStream_list:
        break
