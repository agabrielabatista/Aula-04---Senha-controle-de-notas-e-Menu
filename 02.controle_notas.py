nome = input("Digite seu nome: ")

nota = float(input("Digite sua nota: "))

quantidade_de_notas = 1
soma_das_notas = nota

resposta = input("Deseja adicionar outra nota? ")

while resposta == "sim":
    nota = float(input("Digite outra nota: "))

    soma_das_notas += nota
    quantidade_de_notas += 1

    resposta = input("Deseja adicionar outra nota? ")

media = soma_das_notas / quantidade_de_notas

print(f"{nome}, sua média é {media}")

if media >= 5:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")
