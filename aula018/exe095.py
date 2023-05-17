jogador = {}
jogadores = []
gols = []
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for g in range(0, tot):
        partida = int(input(f" Quantos gols na partida {g}? "))
        partidas.append(partida)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input(f"Quer continuar? ")).upper().strip()[0]
        if continuar in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if continuar == "N":
        break
print("-=" * 30)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-" * 40)
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"Não existe jogador com código {busca}!")
    else:
        print("-- LEVANTAMENTO DO JOGADOR",
              jogadores[busca]["nome"], ":")
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f" No {i + 1} fez {g} gols. ")
        print("-" * 40)
print("<<< VOLTE SEMPRE >>>")
