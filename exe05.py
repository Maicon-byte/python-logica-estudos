idade = int(input("Digite seu idade: "))
pergunta = input("Você tem carteira de motorista? (s/n)")

if idade >= 18 and pergunta == "s":
  print("Você pode dirigir.")
else:
  print("Você não pode dirigir.")
