senha_correta = "python123"
senha = ""
contador = 0
tentativa = 3

while senha_correta != senha and contador <=2:
  senha = input("Digite a senha correta: ")
  contador = contador + 1
  tentativa = tentativa - 1
  if senha == senha_correta:
    print("Acesso permitido.")
  else:
    print("Acesso negado! Voce tem mais", tentativa, "tentativa.")