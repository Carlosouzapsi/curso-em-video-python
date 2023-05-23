# onde eu vou importar as funções do arquivo uteis.py

# programa principal
import uteis  # melhor pratica!
# importando funções de forma separada
# from uteis import fatorial, dobro (não precisa usar o uteis.dobro, só chamar direto)
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)  # chama a função importada com o .
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {uteis.dobro(num)}")
