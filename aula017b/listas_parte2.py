# LISTAS COMPOSTAS (Listas dentro de listas)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)

# Lembre-se sempre de fazer uma cópia se for alterar uma estrutura
galera.append(teste[:])  # cópia da lista teste original
teste[0] = 'Mudei esse elemento'  # Mudei esse elemento
teste[1] = "Mudei esse outro elemento"
print('Fiz a cópia aqui e dei um append...')
galera.append(teste[:])  # fiz a copia aqui
print(f'Depois de dar um append printei aqui: {galera}')

print("Novo exemplo de estrutura composta: ")
galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera)
print(galera[1])
print(galera[1][1])
print(galera[2][1])

print('printando as infos com for: ')

print("se eu quiser brincar com os dados da galera: ")
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade...")


print("Populando uma lista com outra lista composta input de dados: ")
galera = list()
dado = list()

for c in range(0, 2):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])  # fiz a copia pra evitar problemas no python
    # excluindo a lista de dados pra evitar problemas
    dado.clear()
print(galera)

totmai = totmen = 0
print("Mostrando dados da galera maior de 21 anos: ")
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade.")
