n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print("""
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        """)
    opcao = int(input('Qual é a sua opção? '))
    print('-=-=' * 10)
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos números é igual a {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação dos números é igual a {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'O maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando..')
    else:
        print('Opção inválida, tente novamente')
    print('-=-=' * 10)
print('FIM DO PROGRAMA!  Volte sempre!')
