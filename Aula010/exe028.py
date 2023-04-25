from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print(f'O número escolhido foi {computador}, parabéns você venceu.')
else:
    print(f'Você errou o número era {computador}, tente de novo!')
