import socket
import select
import sys
from thread import *


def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!")
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + "> " + message)
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for conn in list_of_conns:
        if conn != connection:
            try:
                conn.send(message)
            except:
                conn.close()
                remove(conn)


def remove(connection):
    if connection in list_of_conns:
        list_of_conns.remove(connection)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 12345
server.bind(('', Port))
server.listen(100)

list_of_conns = []

while True:
    conn, addr = server.accept()
    list_of_conns.append(conn)
    print(str(addr) + " connected")
    start_new_thread(clientthread, (conn, addr))
    conn.close()
server.close()
