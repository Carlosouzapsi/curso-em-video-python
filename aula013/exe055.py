maior_peso = 0
menor_peso = 0
for p in range(0, 5):
    peso = float(input(f'Informe o peso da pessoa {p}: '))
    if peso == 1:  # verifica a primeira ocorrencia, sempre tem o mesmo valor..
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'{maior_peso}')
print(f'{menor_peso}')
