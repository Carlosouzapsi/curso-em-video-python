# O console sempre tentará imprimir uma exceção relativa a um erro:
# print(x)  # dará erro! -> NameError
# n = int(input("Digite um valor inteiro: "))  # usar a string "oito"
# print(n)  # dará erro! -> valueError
# a = int(input("Numerador: "))  # usar valor diferente de 0
# b = int(input("Denominador: "))  # usar o valor zero
# r = a / b
# print(f"O resultado é {r}")  # dará erro! -> ZeroDivisionError
# r = 2 / '2' -> se printar dará TypeError
# lista = [3, 6, 4]
# print(lista[3])  # Dará erro -> IndexError

# Python tem uma lista vasta de exceções..

# Exceções do python herdam da classe mãe Exception

# Usando o try e except

try:
    a = int(input("Numerador: "))  # usar valor diferente de 0
    b = int(input("Denominador: "))  # usar o valor zero
    r = a / b
# except: # comentar todos os outros e descomentar esse pra teste
#     print("Infelizmente tivemos um problema =( ")
except Exception as erro:  # usar no lugar do except sozinho
    print(f"Problema encontrado foi {erro.__class__}")
    print(f"Problema encontrado foi {erro.__cause__}")
except (ValueError, TypeError):
    print("Tivemos um problema com os dados que você digitou")
except ZeroDivisionError:
    print("Não é possivel dividir por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
else:
    print(f"O resultado é {r}")
finally:  # este bloco sempre executará
    print("Volte sempre muito obrigado!")
