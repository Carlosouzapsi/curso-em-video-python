jogador = dict()

jogador['nome'] = str(input("Nome do jogador: "))
tot_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
jogador['gols'] = []
jogador['total'] = 0
tot_gols = 0
for t in range(0, tot_partidas):
    gols = int(input(f'Quantos gols na partida {t}? '))
    tot_gols += gols
    jogador['gols'].append(gols)
jogador['total'] = tot_gols
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print("-=" * 30)
print(f'O jogador {jogador["nome"]} jogou {tot_partidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f"=> Na partida {i}, fez {v}")
print(f"Foi um total de {jogador['total']}")
