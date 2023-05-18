from time import sleep
# hint: Usar o flush pra n criar o buffer e lockar o programa no sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}, ", end=" ", flush=True)
            sleep(0.5)
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}, ", end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")


contador(0, 10, 1)
contador(10, 0, -2)
print("-=" * 30)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("-=" * 30)
contador(inicio, fim, passo)
