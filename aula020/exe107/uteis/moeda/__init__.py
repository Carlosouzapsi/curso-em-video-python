def aumentar(valor, taxa):
    aumenta = (valor * taxa/100) + valor
    return aumenta


def diminuir(valor, taxa):
    diminui = valor - (valor * taxa/100)
    return diminui


def metade(valor):
    metade = valor / 2
    return metade


def dobro(valor):
    dobrar = valor * 2
    return dobrar
