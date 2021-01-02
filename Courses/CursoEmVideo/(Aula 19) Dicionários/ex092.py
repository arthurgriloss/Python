from datetime import date
dic = dict()
dic['Nome'] = input('Nome: ')
dic['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
dic['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dic['ctps'] != 0:
    dic['Contratação'] = int(input('Ano de Contratação: '))
    dic['Salário'] = float(input('Salário: R$'))
    dic['Aposentadoria'] = dic['Idade'] + dic['Contratação'] + 35 - date.today().year
print('')
for k, v in dic.items():
    print(f'''{k} tem o valor {v}''')
