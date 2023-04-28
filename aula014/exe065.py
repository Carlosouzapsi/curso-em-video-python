resp = 'S'
qtd_numeros = 0
soma = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    n = int(input('Informe um número inteiro: '))
    soma += n
    qtd_numeros += 1
    if n == 1:  # verifica a primeira ocorrencia, sempre tem o mesmo valor..
        maior = n
        menor = n
    else:
        if n > menor:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / qtd_numeros
print(f'Você digitou {qtd_numeros} números.')
print(f'A média dos valores lidos é igual a {media}')
print(f'O maior valor lido foi {maior}')
print(f'O menor valor lido foi {menor}')
