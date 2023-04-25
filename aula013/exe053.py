# jogo direto para maiusc.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # separa as palavras em um array
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitiada não é um palindromo!')

# MODO PLATONICOOOOOOO
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # separa as palavras em um array
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
print(f'O incweso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
