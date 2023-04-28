# c = 1
# EXEMPLO SIMPLIFICADO, BOM PARA SITUAÇÕES EM QUE N SE SABE O LIMITE
# while c < 10:
#     print(c)
#     c += 1
# print('FIM!')
# BOM PARA SITUAÇÕES EM QUE N SE SABE O LIMITE
# n = 1
# while n != 0:  # repete até o valor 0 ser digitado (flag, condição de parada)
#     n = int(input('Digite um valor: '))
# print('FIM!')

# r = 'S'  # flag R criada
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar [S/N]')).upper()
# print('FIM!')

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares')
print(f'Você digitou {impar} números impares')
