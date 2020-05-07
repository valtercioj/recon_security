import socket
import sys
port = (20,21,22,23,25,53,80,110,156,161,179,443,1723,1863,3128,3389,8080)

def scan():
	for porta in port:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex((ip, porta)) == 0:
			print(f'Porta {porta} [ABERTA]')
			s.close()
try:
	ip = sys.argv[1]
	scan()
except:
    print('Use python portscan.py ip')
    sys.exit(0)