totlidos = 6
somaPar = 0
for n in range(0, totlidos):
    numero = int(input(f'Digite o {n + 1}o numero: '))
    if numero % 2 == 0:
        somaPar += numero
print(f'A soma dos números pares é {somaPar}')
