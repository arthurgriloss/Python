frase = str(input('Digite uma frase:')).strip().upper()
print('A letra a aparece {} vezes na sua frase'.format(frase.count('A')))
print('A primeira vez que a parece é na posição:', frase.find('A')+1)
print('A ultima vez que aparece é na posição:', frase.rfind('A')+1)
