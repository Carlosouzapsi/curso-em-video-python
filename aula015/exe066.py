qtd_numeros = soma = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    qtd_numeros += 1
    soma += n
print(f'A soma entre os números digitados é: {soma}')
print(f'A quantidade de números digitados é: {qtd_numeros}')
