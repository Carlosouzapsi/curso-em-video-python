from time import sleep


def maior(*params):
    print("-=" * 30)
    print("Analisando os valores passados...")
    for v in params:
        print(v, end=" ", flush=True)
        sleep(0.5)
    print(f"Foram informados {len(params)} valores ao todo ")
    maior = 0
    for m in params:
        if m == 0:
            maior = m
        else:
            if maior < m:
                maior = m
    print(f"O maior valor informado foi {maior}.")


    # Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
