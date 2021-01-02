from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano que você nasceu: '))
cat = ano - nascimento
print('O atleta tem {} anos'.format(cat))
if cat <= 9:
    print('CLASSIFICAÇÂO: MIRIN')
elif cat <= 14:
    print('CLASSIFICAÇÂO: INFANTIL')
elif cat <= 19:
    print('CLASSIFICAÇÂO: JUNIOR')
elif cat <= 25:
    print('CLASSIFICAÇÂO: SÊNIOR')
else:
    print('CLASSIFICAÇÂO: MASTER')
