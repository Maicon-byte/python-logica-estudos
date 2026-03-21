numero_correto = 0
numero = None

while numero_correto != numero:
  numero = int(input("Digite o número '0': "))
  if numero == numero_correto:
    print("Muito bom! Meus parabéns")
  else:
    print("Não foi isso que eu pedi. Tente novamente.")
