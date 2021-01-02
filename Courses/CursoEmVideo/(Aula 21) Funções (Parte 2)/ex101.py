from datetime import date


def voto(nascimento):
    idade = date.today().year - nascimento
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL'
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    if idade < 18:
        return f'Com {idade} anos: VOTO NEGADO'


print(voto(int(input('Em que ano você nasceu? '))))
