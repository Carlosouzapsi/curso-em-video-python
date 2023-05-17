pessoa = dict()
pessoas = list()

while True:
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print("Erro! Responda apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    pessoas.append(pessoa.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N]")).upper()[0]
        if continuar in "SN":
            break
        print("Erro! Reponda apenas S ou N.")
    if continuar == 'N':
        break
print("-=" * 30)
print(f"Ao todo temos {len(pessoas)} pessoa(s) cadastradas.")
soma_idades = 0
for p in range(0, len(pessoas)):
    soma_idades += pessoas[p]['idade']
media = soma_idades / len(pessoas)
print(f'A média de idade é de {media:5.2f}')
lista_mulheres = []
for f in range(0, len(pessoas)):
    if pessoas[f]['sexo'] in 'F':
        lista_mulheres.append(pessoas[f]['nome'])
print(f"As mulheres cadastradas foram:", end=' ')
for f in range(0, len(lista_mulheres)):
    print(f"{lista_mulheres[f]}", end=' ')
print()
idade_acima = []
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        idade_acima.append(pessoas[i])
for i in range(0, len(idade_acima)):
    print(
        f"nome = {idade_acima[i]['nome']}; sexo = {idade_acima[i]['sexo']}; idade = {idade_acima[i]['idade']}")
print("PROGRAMA ENCERRADO!")

# Outra forma de exibir idades acima da media:
# for p in pessoas:
#     if p['idade'] >= media:
#         print("  ")
#         for k, v in p.items():
#             print(f"{k} = {v}; ", end="")
#         print()
# print("<< ENCERRADO >>")
