peso=float(input("Digite o peso"))

if peso >= 90:
    print("Acima")
elif peso < 90 and peso >= 85:
    print("Ta proximo")
else:
    print("Ta normal")