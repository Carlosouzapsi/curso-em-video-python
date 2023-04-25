# num = int(input('Informe um número: '))
# # usar como input 1834
# n = str(num)
# print(f'Analisando o número:  {num}')
# print(f'Unidade: {n[3]}')
# print(f'Dezena: {n[2]}')
# print(f'Centena: {n[1]}')
# print(f'Milhar: {n[0]}')

num = int(input('Digite um número: '))
u = num // 1 % 10  # padrão unidade
d = num // 10 % 100  # padrão dezena
c = num // 100 % 10  # padrão centena
m = num // 1000 % 10  # padrão milhar
print(f'Analisando o número: {u}')
print(f'Analisando o número: {d}')
print(f'Analisando o número: {c}')
print(f'Analisando o número: {m}')
