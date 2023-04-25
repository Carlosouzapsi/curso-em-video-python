# co = float(input("Comprimento do cateto oposto: "))
# ca = float(input("Comprimento do cateto adjacente: "))
# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa vai medir {hipotenusa}')

# Usando módulos
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hipotenusa}')
