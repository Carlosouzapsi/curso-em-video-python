numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp in "N":
        break
print(f"Foram digitados e inseridos na lista {len(numeros)} valores")
numeros.sort(reverse=True)
print(f"Lista de forma decrescente: {numeros}")
if 5 in numeros:
    print(f"O valor 5 está presente na lista")
else:
    print(f"O valor 5 não está na lista")
