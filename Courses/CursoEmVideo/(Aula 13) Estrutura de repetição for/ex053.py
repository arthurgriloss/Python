frase = input('Digite uma frase: ').strip().upper()
junto = frase.split()
novaFrase = ''.join(junto)
inverso = ''
for i in range(len(novaFrase) - 1, -1, -1):
    if novaFrase[i] != ' ':
        inverso += novaFrase[i]
print('''A frase escrita foi {}
A frase gerada foi {}'''.format(frase, inverso))
if novaFrase == inverso:
    print('A frase é um POLINDROMO')
else:
    print('A frase não é um POLINDROMO')
