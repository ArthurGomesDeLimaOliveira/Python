soma = 0
i = 0
while i < 7:
    idade = float(input("Idades:"))
    i+=1
    soma = idade + soma
media = soma/7
print("{:.2f}".format(media))
