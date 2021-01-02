from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
if ano == nascimento +18:
    print('''Está na hora de se alistar
    Por favor compareça a zona de alistamento mais proxima''')
elif ano < nascimento +18:
    print('''Ainda não está da hora de se alistar
    Ainda faltam {} anos'''.format(nascimento + 18 - ano))
else:
    print('''Ja passou da hora de se alistar!!
    Você deveria ter se alistado a {} anos'''.format(ano - (nascimento + 18)))
