r1 = float(input('Primeiro segumento: '))
r2 = float(input('Primeiro segumento: '))
r3 = float(input('Primeiro segumento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos fornecidos podem sim formar um triângulo!')
    # if r1 == r2 and r2 == r3: (forma elegante pythonica)
    if r1 == r2 == r3:
        print(f'O triângulo é equilátero')
    if r1 != r2 != r3 != r1:
        print(f'O triânfulo é escaleno!')
    else:
        print(f'O triângulo é Isósceles!')
else:
    print('Os segmentos fornecidos não podem formar um triângulo!')
