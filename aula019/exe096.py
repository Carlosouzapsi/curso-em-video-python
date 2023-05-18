def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg}x{comp} é de {a}m2")


# programa principal
print(" Controle de terrenos ")
print("-" * 20)
base = float(input("Largura (m): "))
altura = float(input("Comprimento (m): "))
area(base, altura)
