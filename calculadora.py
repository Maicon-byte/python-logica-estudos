num1 = None

def menu():
  print("==== Calculadora ====")
  print("1 - Somar")
  print("2 - Subtrair")
  print("3 - Multiplicar")
  print("4 - Dividir")
  print("0 - Sair")

def somar():
  a = int(input("Digite um número: "))
  b = int(input("Digite outro número: "))
  return a + b
  
def sub():
  a = int(input("Digite um número: "))
  b = int(input("Digite outro número: "))
  return a - b

def mult():
  a = int(input("Digite um número: "))
  b = int(input("Digite outro número: "))
  return a * b
  
def div():
  a = int(input("Digite um número: "))
  b = int(input("Digite outro número: "))
  if b == 0:
    return -1
  else:
    return a / b

while num1 != 0:
 
  menu()
  
  num1 = int(input("Qual operação você vai fazer? "))

  if num1 == 1:
    resultado = somar()
    print("A resposta é:",resultado)
  
  elif num1 == 2:
    resultado = sub()
    print("A resposta é:",resultado)
    
  elif num1 == 3:
    resultado = mult()
    print("A resposta é:",resultado)
  
  elif num1 == 4:
    resultado = div()
    if resultado == -1:
      print("Divisão por zero, inválida")
    else:
      print("A resposta é:",resultado)
 
  elif num1 == 0:
    print("Obrigado por usar a calculadora")
    
  else:
    print("Opcão inválida,tente de novo!")
