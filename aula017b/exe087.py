matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaTerceiraColuna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=" ")
    print()
print(f"A soma dos pares é {somaPares}")
for l in range(0, 3):
    somaTerceiraColuna += matriz[l][2]
print(f"Soma dos valores da terceira coluna: {somaTerceiraColuna}")
maiorValor = 0
for c in range(0, 3):
    if c == 0:
        maiorValor = matriz[1][c]
    elif matriz[1][c] > maiorValor:
        maiorValor = matriz[1][c]
print(f"O maior valor da segunda linha é: {maiorValor}")
