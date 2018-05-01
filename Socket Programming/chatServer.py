import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 12445
server.bind(('', Port))
server.listen(5)

while True:
    conn, addr = server.accept()
    print(addr[0] + " connected")

    while True:
        inputStream_list = [sys.stdin, conn]

        read_sockets, write_socket, error_socket = select.select(
            inputStream_list, [], [])

        for socks in read_sockets:
            if socks == conn:
                message = socks.recv(2048)
                print("<received>" + repr(message))
            else:
                message = raw_input()
                conn.send(message)
                print("<You>" + repr(message))
            if message == 'bye':
                conn.close()
                inputStream_list.remove(conn)
                break
        if conn not in inputStream_list:
            break
    conn.close()
    # serve the next client
server.close()
