numero = int(input('Digite um número inteiro : '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
# Utilizar conversores automáticos do python dentro da própria linguagem:
if opcao == 1:
    print(f'{opcao} para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{opcao} para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{opcao} para OCTAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente!')
