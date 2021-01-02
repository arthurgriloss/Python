def maior(* num):
    maior = cont = 0
    print('-'*60)
    print('Analisando os valores...')
    for c in num:
        print(num, end=' ')
        if num > maior:
            maior = num
    cont += 1
    print(f'''Foram informados {cont} valores ao todo
O maior valor informado foi {maior}''')


# main program
maior(3, 5, 7, 9, 10)
maior(0, 1, 9, 8)
maior(2, 9)
maior()
