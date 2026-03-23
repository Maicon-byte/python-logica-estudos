# Exercicio 02 + Opcional
numeros = []
def lista():
  numeros = []
  for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)
  return numeros  

def maior(lista):
 print("Maior:", max(lista))
 print("Menor:", min(lista))
 print("Soma:", sum(lista))
 print("Média:", sum(lista) / len(lista))
 
numeros = lista()
maior(numeros)