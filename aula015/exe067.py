while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n < 0:
        print('Programa sendo encerrado!')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
