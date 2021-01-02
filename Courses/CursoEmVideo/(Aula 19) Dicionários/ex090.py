dic = dict()
dic['Nome'] = input('Nome: ')
dic['Media'] = float(input(f'Media de {dic["Nome"]}: '))
if dic['Media'] >= 7:
    dic['Situação'] = 'Aprovado'
else:
    dic['Situação'] = 'Reprovado'
for k, e in dic.items():
    print(f'{k} é igual a {e}')
