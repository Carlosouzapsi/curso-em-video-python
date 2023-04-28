# Usando o módulo factorial do próprio python
# from math import factorial

# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print(f'Modo moderno -> O fatorial de {n} é {f}.')

# modo tradicional
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {c}! = ', end='')
while c > 0:
    print(f'{c}', end='')  # end para n pular de linha!
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
