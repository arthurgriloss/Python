from time import sleep
soma = 0
nMulheres = 0
saveNome = ' '
saveIdade = 0
c = 0
for i in range(0, 4):
    print('----- {}ª pessoa -----'.format(i+1))
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    genero = input('Digite seu genero: [m/f] ').upper()
    soma = soma + idade
    if genero == 'M' and idade > saveIdade:
        saveIdade = idade
        saveNome = nome
    if genero == 'F' and idade < 20:
        c = c + 1
print('-'*20)
print('Analisando', end='')
for i in range(0, 3):
    print('.', end='')
    sleep(1)
print('')
print('-'*20)
print('''A média de idade do grupo é {:.0f}
O nome do homem mais velho tem {} anos e se chama {}
{} mulheres tem menos de 20 anos'''.format(soma/4, saveIdade, saveNome, c))
