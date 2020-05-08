import requests
import sys
from socket import *

def ip():
	ip = gethostbyname(site)
	return ip
def bruteForce():

	arq = open('rato.txt','r')
	
	for dns in arq:
		dns = dns.replace('\n','')
		result = "http://"+dns+site
		url = result.replace('http://','')
		try:
			resposta = requests.get(result)
			resposta = (resposta.status_code)
			
			if resposta == 200:
				print('HOST ENCONTRADO: '+url,'===> IP: '+ip())
				
		except:
			continue
		arq.close()		
print(r'''
____________ _   _ _____ _____  ______ ___________  _____  _____  ______ _   _  _____ 
| ___ \ ___ \ | | |_   _|  ___| |  ___|  _  | ___ \/  __ \|  ___| |  _  \ \ | |/  ___|
| |_/ / |_/ / | | | | | | |__   | |_  | | | | |_/ /| /  \/| |__   | | | |  \| |\ `--. 
| ___ \    /| | | | | | |  __|  |  _| | | | |    / | |    |  __|  | | | | . ` | `--. \
| |_/ / |\ \| |_| | | | | |___  | |   \ \_/ / |\ \ | \__/\| |___  | |/ /| |\  |/\__/ /
\____/\_| \_|\___/  \_/ \____/  \_|    \___/\_| \_| \____/\____/  |___/ \_| \_/\____/ 
                                                                                      
##################################                                                                                      
          version : 1.0               
     author : valtercio junior    
##################################
		



		''')

try:
	site = sys.argv[1]
	bruteForce()
except:
	print(' Use: python dnsrato.py site.com.br ')
	exit()


	

