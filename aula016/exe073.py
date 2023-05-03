times_brasileirao = ('Flamengo', 'Palmeiras', 'Atlético-MG', 'Fortaleza', 'Corinthians', 'Internacional', 'Fluminense', 'São Paulo', 'Cuiabá',
                     'Sport', 'Santos', 'Juventude', 'Bahia', 'Athletico-PR', 'Ceará', 'América-MG', 'Grêmio', 'Atlético-GO', 'Chapecoense', 'Coritiba')
# A)
print('=' * 50)
print('5 Primeiros colocados: ')
for pos, time in enumerate(times_brasileirao):
    if pos == 5:
        break
    print(f'{pos + 1}) {time}')
print('=' * 50)
# B) Usando o método de fatiar, daria pra fazer com for
print('=' * 50)
print(times_brasileirao[16:])
print('=' * 50)
# C) Times em ordem alfabética
print('=' * 50)
print(sorted(times_brasileirao))
print('=' * 50)
# D) Posição, time chapecoense
print('=' * 50)
print('Posição da Chapecoense: ',  times_brasileirao.index(
    'Chapecoense') + 1, ' posição')
print()
print('=' * 50)
