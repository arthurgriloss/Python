nome = str(input('Digite seu nome completo: ')).strip()
nomeSplit = nome.split()
print('Seu primeiro nome é: ', nomeSplit[0])
posUltimoNome = nome.rfind(' ')
print('Seu ultimo nome é:', nome[posUltimoNome:])#ou nome(len(nome)-1)
