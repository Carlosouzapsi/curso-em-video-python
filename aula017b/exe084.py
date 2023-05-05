pessoas = []
pessoa = []
maior = menor = 0
while True:
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Digite o peso da pessoa: '))
    pessoa.append(nome)
    pessoa.append(peso)
    if len(pessoas) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    # pega cópia da lista pra evitar que o python se perca
    pessoas.append(pessoa[:])
    # dar um clear na lista pessoa pq ela é temporária
    pessoa.clear()
    cont = str(input("Quer continuar? ")).strip().upper()[0]
    if cont in "N":
        break
print(f"Os dados das pessoas pessoas cadastradas foram: {pessoas}")
print(f"Foram cadastradas um total de {len(pessoas)} pessoa(s)")
print(f"O maior peso foi de {maior}kg")
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f"O menor peso foi de {menor}kg")
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')
