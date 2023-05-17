jogador = {}
jogadores = []
gols = []
tot_gols = 0
while True:
    jogador['nome'] = str(input("Nome do jogador: "))
    qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for g in range(0, qtd_partidas):
        qtd_gols = int(input(f" Quantos gols na partida {g}? "))
        tot_gols += qtd_gols
        gols.append(qtd_gols)
    jogador['gols'] = gols[:]
    jogador['total'] = tot_gols
    jogadores.append(jogador.copy())
    gols.clear()
    # print(f"printei aqui: {jogadores}")
    continuar = str(input(f"Quer continuar? ")).upper().strip()
    if continuar in "N":
        break
print("-=" * 30)
print(f'{"cod":<4}{"nome":<10}{"gols":>4}{"total":>8}')
print(jogadores)
# for i, v in enumerate(jogador['gols']):

# for k, v in jogador.items():

# Outra forma de exibir idades acima da media:
# for p in pessoas:
#     if p['idade'] >= media:
#         print("  ")
#         for k, v in p.items():
#             print(f"{k} = {v}; ", end="")
#         print()
# print("<< ENCERRADO >>")
