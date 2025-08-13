soma = 0
for i in range(1,6):
    print(i)
    periodo = float(input("Digite o periodo:"))
    salario = int(input("Digite o salario"))

    if periodo == 3 or periodo == 5:
        soma = soma + salario

print("Soma dos salarios: ",soma)