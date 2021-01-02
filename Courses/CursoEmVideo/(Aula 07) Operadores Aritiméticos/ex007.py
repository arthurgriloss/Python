print('qual é a media das notas do aluno?')
nota1 = float(input('digite a nota 1:'))
nota2 = float(input('digite a nota 2:'))
nota3 = float(input('digite a nota 2:'))
print('a média da nas notas {}, {}, e {} é: {}'.format(nota1, nota2, nota3, (nota1+nota2+nota3)/3))
if (nota1+nota2+nota3)/3 >= 5:
    print('voce foi aprovado')
else:
    print('voce foi reprovado')

