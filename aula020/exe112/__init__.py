from utilidadesCeV import moeda
from utilidadesCeV import dado

preco = dado.leiaDinheiro(f"Digite o preço: R$")
moeda.resumo(preco, 80, 35)
