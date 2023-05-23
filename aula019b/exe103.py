def ficha(nome="<desconhecido>", gols=0):
    print(f"O Jogador {nome} fez {gols} gol(s) no campeonato.")


# Programa principal
nome = str(input("Informe o nome do jogador: "))
gols = str(input("Informe a quantidade de gols: ")).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gols=0)
else:
    ficha(nome, gols)
