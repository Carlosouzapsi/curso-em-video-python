print('Gerador de PA')
print("-=" * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} mostrados.')
