def aumentar(valor=0, taxa=0, format=False):
    aumenta = (valor * taxa/100) + valor
    # outro jeito de escrever o return
    # return aumenta if format is False else moeda(valor)
    if format == True:
        aumenta = moeda(aumenta)
    return aumenta


def diminuir(valor=0, taxa=0, format=False):
    diminui = valor - (valor * taxa/100)
    if format == True:
        diminui = moeda(diminui)
    return diminui


def metade(valor=0, format=False):
    metade = valor / 2
    if format == True:
        metade = moeda(metade)
    return metade


def dobro(valor=0, format=False):
    dobrar = valor * 2
    if format == True:
        dobrar = moeda(dobrar)
    return dobrar


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:>.2f}".replace('.', ',')


def resumo(preco=0, taxaa=0, taxar=0):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{dobro(preco, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}")
    print(f"{taxar}% de redução: \t{diminuir(preco, taxar, True)}")
    print("-" * 30)
