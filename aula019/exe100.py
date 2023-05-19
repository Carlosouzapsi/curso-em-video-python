from random import randint
from time import sleep


def sorteia(lista):
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        sleep(0.3)
    print(f"Sorteando 5 valores da lista: {lista} ", end="", flush=True)
    print("PRONTO!")


def somaPar(lista):
    somaPares = 0
    for p in lista:
        if p % 2 == 0:
            somaPares += p
    print(f"Somando os valores pares de: {lista}, temos {somaPares}")


numeros = list()
sorteia(numeros)
somaPar(numeros)
