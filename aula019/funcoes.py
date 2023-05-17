# exemplos básicos:
def saudacao():
    print("Olá mundo!")
# criando uma função para somar dois numeros:


def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")
    print(s)


# programa principal - passando parametros
soma(a=4, b=5)
soma(b=4, a=5)
soma(8, 9)  # n explicito
soma(2, 1)  # n explicito
# soma(2, 1, 3)  # vai dar erro, n tem param declarado...

# empacotamento de parametros..

# * irá desempacotar os parametros


def contador(*num):
    for valor in num:
        print(f"{valor}", end=" ")
    print("FIM!")


def contador_len(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

contador_len(2, 1, 7)
contador_len(8, 0)

# criando uma função especifica pra um program
valores = [6, 3, 1, 0, 2]


def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


dobra(valores)
print(f"valores dobrados {valores}")


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")


soma(5, 2)
soma(2, 9, 4)
