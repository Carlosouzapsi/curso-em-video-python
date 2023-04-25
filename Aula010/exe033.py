# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# if a < b and a < c:
#     menor = a
# if b < c and b > a:
#     menor = b
# if c < a and c < b:
#     menor = c

# print(f'O menor número é {menor}')

# Forma mais pythonica de se fazer:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificação quem é o maior
maior = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    menor = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
