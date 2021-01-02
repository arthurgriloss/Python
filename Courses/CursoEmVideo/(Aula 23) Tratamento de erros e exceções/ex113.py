def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        else:
            return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o valor real digitado foi {real:.1f}')