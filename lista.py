numeros = []

def menu():
    print("\n1 - Adicionar número")
    print("2 - Ver lista")
    print("3 - Ver soma")
    print("4 - Ver média")
    print("5 - Ver maior")
    print("0 - Sair")

def pedir(msg):
    return int(input(msg))

def somar(lista):
    return sum(lista)

def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def maior(lista):
    if len(lista) == 0:
        return None
    return max(lista)

while True:
    menu()
    num = pedir("Escolha uma opção: ")

    if num == 1:
        n = pedir("Digite um número: ")
        numeros.append(n)

    elif num == 2:
        print("Lista:", numeros)

    elif num == 3:
        print("Soma:", somar(numeros))

    elif num == 4:
        print("Média:", media(numeros))

    elif num == 5:
        print("Maior:", maior(numeros))

    elif num == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida")