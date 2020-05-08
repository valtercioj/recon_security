import requests
import sys
def recon():

	arq = open('wordlist.txt','r')
	
	for domain in arq:
		domain = domain.replace('\n','')
		result = f"http://{site}/{domain}"
		
		try:
			resposta = requests.get(result)
			resposta = (resposta.status_code)
			
			if resposta == 200:
				print('Diretorio Encontrado: '+domain)

		except:
			continue
		arq.close()

try:
	site = sys.argv[1]
	recon()
except:
	print(' Use: python domain.py www.site.com.br ')
	exit()
