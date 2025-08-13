idade=float(input("Digite a idade:"))
peso=float(input("Digite o peso:"))

if idade < 20:
    if peso < 60:
        print("9")
    elif peso >= 60 and peso <= 90:
        print("8")
    elif peso > 90:
        print("7")

if idade >= 20 and idade <=50:
    if peso < 60:
        print("6")
    elif peso >= 60 and peso <= 90:
        print("5")
    elif peso > 90:
        print("4")

if idade > 50:
    if peso < 60:
        print("3")
    elif peso >= 60 and peso <= 90:
        print("2")
    elif peso > 90:
        print("1")