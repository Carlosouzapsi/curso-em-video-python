print('Gerador de PA')
print("-=" * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
c = 1
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    c += 1
print(' FIM!')
