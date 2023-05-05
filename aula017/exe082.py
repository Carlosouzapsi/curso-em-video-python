numeros = []

while True:
    numero = int(input("Informe um número: "))
    numeros.append(numero)
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if continuar in 'N':
        break
print(f"Lista inteira: {numeros}")
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)
print(f"Lista de números pares: {pares}")
print(f"Lista de números impares: {impares}")
