import socket
import select
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '127.0.0.1'
Port = 12445
s.connect((IP_address, Port))

while True:
    inputStream_list = [sys.stdin, s]

    read_sockets, write_socket, error_socket = select.select(
        inputStream_list, [], [])

    for socks in read_sockets:
        if socks == s:
            message = socks.recv(2048)
            print("<received>" + message)
        else:
            message = input("Enter text to send")
            s.send(repr(message))
            print("<You>" + message)
            if message == 'bye':
                s.close()
                inputStream_list.remove(s)
                break
    if s not in inputStream_list:
        break
s.close()
