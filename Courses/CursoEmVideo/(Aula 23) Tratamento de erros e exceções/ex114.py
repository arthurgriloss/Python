import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
    print('Site acessado com sucesso')
except:
    print('Falha ao acessar o site')