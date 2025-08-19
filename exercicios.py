i=0
count=0

while i < 20:
    idade=int(input("Digite a idade dos atletas"))
    if idade > 17:
        count+=1
    i+=1
print("Jogadores com idade maiores que 17:",count)