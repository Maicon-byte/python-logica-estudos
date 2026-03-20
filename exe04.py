hora = int(input("Digite a hora atual: "))

if hora >= 5 and hora <= 11:
  print("Bom dia")
  
elif hora >= 12 and hora <= 17:
  print("Boa tarde")
  
elif hora >= 18 and hora<= 22:
  print("Boa noite")
  
elif hora >= 23 or hora <= 4:
  print("Hora de dormir")
  
else:
  print("Hora inválida.")