def ajuda(com):
    help(com)


# programa principal
while True:
    comando = input('Função ou Bibiloteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)