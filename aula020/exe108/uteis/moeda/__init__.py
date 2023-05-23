def aumentar(valor=0, taxa=0):
    aumenta = (valor * taxa/100) + valor
    return aumenta


def diminuir(valor=0, taxa=0):
    diminui = valor - (valor * taxa/100)
    return diminui


def metade(valor=0):
    metade = valor / 2
    return metade


def dobro(valor=0):
    dobrar = valor * 2
    return dobrar


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:>.2f}".replace('.', ',')
