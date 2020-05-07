import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "200.160.2.3"
port = 43
s.connect((ip,port))
s.send(sys.argv[1]+'\r\n')
resp = s.recv(1024)
print resp