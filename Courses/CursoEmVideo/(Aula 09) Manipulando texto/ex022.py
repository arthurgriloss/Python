nome = input('Digite seu nome completo:').strip()
print('Seu nome completo em Maiusculo é:', nome.upper())
print('Seu nome completo em minusculo é:', nome.lower())
print('Seu nome tem no total {} letras'.format(len(nome)-nome.count(' ')))
nomeSplit = nome.split()
print('Seu primeiro nome é:', nomeSplit[0])