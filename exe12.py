numeros = []
maior = 0
soma = 0

for i in range(5):
  n = int(input("Digite um número: "))
  numeros.append(n)
  
  soma = soma + numeros[i]
 
  if numeros[i] > maior:
   maior = numeros[i] 
   
  if numeros[i] < menor:
   menor = numeros[i] 

media = soma / 5
  
print("Lista:",numeros)
print("Maior número: ",maior)
print("Menir número: ",menor)
print("Total da soma: ",soma)
print("Média: ",media)

