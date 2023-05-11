from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print("Valores sorteados: ")
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# ordenando o ranking:
# itemgetter com parametro zero ordena o dicionario pela chave e parametro 1 ordena via value
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# virou uma lista! =O
print("-=" * 30)
# é necessário percorrer com um for com uma lista
for i, v in enumerate(ranking):
    print(f"{i + 1}o lugar: {v[0]} com {v[1]}.")
    sleep(1)
