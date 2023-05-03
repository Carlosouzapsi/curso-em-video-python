numeros = (int(input('Informe um número: ')), int(input('Informe outro número: ')), int(
    input('Informe mais um número: ')), int(input('Informe o ultimo número: ')))

print(f'O valor 9 apareceu {numeros.count(9)}')
if 3 in numeros:
    print(
        f'O primeiro valor 3 foi digitado na posição: {numeros.index(3) + 1}')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição...')

print(f'O valores pares digitados foram: ')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')
