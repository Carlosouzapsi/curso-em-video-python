# Ajuda interativa no python: help()
# help()
# Docstring (Strings de documentação) :


# def contador(i, f, p):
#  """"
#     -> Faz uma contagem e mostra na trela
#     inicio -> i
#     fim -> f
#     passo -> p
#     """
#   c = i
#    while c <= f:
#         print(f"{c}", end="")
#         c += p
#     print('Fim!')
# # help(contador)
# ##############################
# # Parametros opcionais:
# def somar(a, b, c=0):  # c é opcional a função n quebra
#     # todos os valores podem ter um opcional atribuido.
#     s = a + b + c
#     print(f"A soma vale {s}")

# somar(3, 2)
# somar(8, 4, 3)  # o valor opcional é sobreescrito
# somar(b=3, c=1, a=3)  # reordenando a vontade

##############################
# Escopo de variáveis
##############################
# def teste():
#     x = 2  # variavel que tá presa no escopo da função!
#     print(f"Na função teste, n vale {n}")


# n = 2
# print(f"No programa principal , n valor {n}")
# # print(f"O valor de x vai dar erro {x}")
# teste()

# Escopo interno n muda externo necessariamente!
def teste(b):
    # global a -> posso forçar o a global a ser usado!
    a = 8  # essa variável é nova diferente da global
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")


a = 5
teste(a)
print(f"A fora vale {a}")

# Usando return para ter mais flexibilidade na formatação!


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


resp1 = somar(3, 2, 5)
resp2 = somar(3, 2)
resp3 = somar(1)
print(f"A soma é {resp1}")
print(f"A soma é {resp2}")
print(f"A soma é {resp3}")


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f  # pode retornar true/false ou strings no só valores numericos..


n = int(input('Digite um número: '))
print(f"O fatorial de {n} é igual a {fatorial(n)}")
