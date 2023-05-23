from uteis import moeda

preco = float(input("Digite o preço: R$"))
print(f"O dobro de R${preco} é R${moeda.dobro(preco):.2f}")
print(f"A metade de R${preco} é R${moeda.metade(preco):.2f}")
print(f"Aumentando 10% temos RS{moeda.aumentar(preco, taxa=10):.2f}")
