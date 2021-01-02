nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Sua média é {:.2f}'.format(media))
if media >= 7:
    print('Você foi aprovado')
elif 7 > media >= 5:
    print('Você está de recuperação')
else:
    print('Você não foi aprovado')
7
