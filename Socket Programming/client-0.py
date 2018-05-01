import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname('www.google.com')

port = 80

s.connect((host, port))
print("socket connected to google http server")
