# dá pra jogar essas funcs pra um modulo tbm, pra organizar melhor
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro! \nDigite um número inteiro válido.\033[m")
            continue  # joga pro laço de novo
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interompida pelo usuario.\033[m")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro! Digite um número real válido.\033[m")
            continue  # joga pro laço de novo
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interompida pelo usuario.\033[m")
            return 0
        else:
            return n


num = leiaInt("Digite um numero inteiro: ")
num = leiaFloat("Digite um numero real: ")
