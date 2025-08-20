def calculaMedia(a,b,c):
    soma = a+b+c
    media = soma/3
    return media

def avaliaResultado(media):
    if media >= 60:
        return "aprovado"
    elif media < 60:
        return "Reprovado"


a = int(input("Digite a"))
b = int(input("Digite b"))
c = int(input("Digite c"))
r = calculaMedia(a,b,c)

mensagem = avaliaResultado(r)
print(mensagem)