soma = 0
contador = 0
maior = None
menor = None
impar = 0
par = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    soma += numero
    contador += 1
    
    if maior is None or numero > maior:
      maior = numero
    if menor is None or numero < menor:
      menor = numero
      
    if numero % 2 == 0:
     par += 1
    else:
     impar += 1

if contador == 0:
    print("Nenhum número digitado.")
    
else:
    media = soma / contador
    print("Soma total:", soma)
    print("Quantidade:", contador)
    print("Média:", media)
    print("Maior:", maior)
    print("Menor:", menor)
    print("Quatidade de números impares:", impar)
    print("Quantidade de números pares:", par)