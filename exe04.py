hora = int(input("Digite a hora atual: "))

if 5 <= hora <= 11:
    print("Bom dia")
elif 12 <= hora <= 17:
    print("Boa tarde")
elif 18 <= hora <= 22:
    print("Boa noite")
elif hora >= 23 or hora <= 4:
    print("Hora de dormir")
else:
    print("Hora inválida.")