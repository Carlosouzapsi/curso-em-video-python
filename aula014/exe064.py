qtd_numeros = 0
soma = 0
n = 0
n = int(input('Informe um número [999 para parar]: '))
while n != 999:
    qtd_numeros += 1
    soma += n
    n = int(input('Informe um número [999 para parar]: '))
print(f'Foram digitados ao todo: {qtd_numeros} números.')
print(f'A soma entre os valores digitados é igual à: {soma}.')
