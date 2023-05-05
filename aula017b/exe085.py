# uma lista só com duas listas dentro como critério
numeros = [[], []]
for c in range(1, 8):
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(numeros)
