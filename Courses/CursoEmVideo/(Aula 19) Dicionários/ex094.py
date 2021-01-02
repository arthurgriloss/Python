lista = list()
dic = dict()
soma = 0
while True:
    dic['nome'] = input('Nome: ')
    while True:
        sexo = input('Sexo [M/F]: ').upper().strip()
        if sexo in 'MF':
            dic['sexo'] = sexo
            break
        else:
            print('ERRO! Digite apenas M ou F')
    dic['idade'] = int(input('Idade: '))
    soma += dic['idade']
    lista.append(dic.copy())
    while True:
        op = input('Quer continuar [S/N]? ').upper().strip()
        if op in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N')
    if op == 'N':
        break
print('-='*30)
print(f'''A) Ao todo temos {len(lista)} pessoas cadastradas
B) A média de idade é {soma/len(lista):.2f}
As mulheres cadastradas foram ''', end='')
for p, e in enumerate(lista):
    if e['sexo'] == 'F':
        print(e['nome'], end=' ')
print('')
for p, e in enumerate(lista):
    if e['idade'] > soma/len(lista):
        print(e)
print('Encerrado')