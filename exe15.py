numeros = []
num = None

def menu():
  print("1 - Adicionar número na lista.")
  print("2 - Ver a lista completa.")
  print("3 - Ver soma total da lista.")
  print("4 - Ver média da lista.")
  print("5 - Ver maior número da lista.")
  print("0 - Sair.")

def pedir():
  n = int(input())
  return n

def somar(lista):
  soma = sum(lista)
  return soma

def media(lista):
  soma = sum(lista)
  return soma / len(lista)

def maior(lista):
  m = max(lista)
  return m

while num != 0:
  print("Escolha uma das opcões: ")
  menu()
  num = pedir()
  
  if num == 1:
    print("Qual números você que adicionar a lista? ")
    n = pedir()
    numeros.append(n)
   
  if num == 2:
    print("Lista de números completa:",numeros)
  
  if num == 3:
    print("A soma total da lista é:",somar(numeros))

  if num == 4:
    print("A média da lista é:", media(numeros))

  if num == 5:
    print("O maior número da lista é:", maior(numeros))