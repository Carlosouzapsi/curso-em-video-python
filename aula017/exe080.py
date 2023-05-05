
numeros = []
for n in range(0, 4):
    numero = int(input('informe um valor: '))
    # 3 possibilidade ou é o maior, ou menor valor ou está no meio
    if n == 0 or numeros[-1]:  # vendo se é maior que ultimo elemento
        numeros.append(numero)
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos += 1
print("=" * 30)
print(f"O valores digitados são: {numeros}")
