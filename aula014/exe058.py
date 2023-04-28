from random import randint

print('SOU SEU COMPUTADOR...')
print('ACABEI DE PENSAR EM UM NUMERO ENTRE 0 E 10')
print('SERÁ QUE VOCÊ CONSEGUE ADVINHAR QUAL FOI?')
acertou = False
palpites = 0
numero = randint(0, 10)
while not acertou:
    palpite = int(input('QUAL O SEU PALPITE? '))
    palpites += 1
    if palpite == numero:
        acertou = True
    else:
        if palpite < numero:
            print('Mais... Tente de novo!')
        elif palpite > numero:
            print('Menos... Tente de novo!')
print(f'ACERTOU COM {palpites} TENTATIVAS, PARABÉNS!')
