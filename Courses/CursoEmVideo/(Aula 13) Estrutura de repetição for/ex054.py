from datetime import date
c = 0
for i in range(0, 7):
    ano = int(input('Digite o ano do seu nascimento da {}ª pessoa: '.format((i+1))))
    if date.today().year - ano >= 21:
        c += 1
print('{} pessoas ja atingiram a maior idade e {} pessoas ainda não atingiram a maior idade'.format(c, 7 - c))
