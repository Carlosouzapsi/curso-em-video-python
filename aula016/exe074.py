from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print("Valores sorteados: ")
for n in numeros:
    print(f"{n} ", end='')
print()
print(f' O maior valor sorteado foi: {max(numeros)}')
print(f' O menor valor sorteado foi: {min(numeros)}')
