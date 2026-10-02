def soma ():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    resultado = num1 + num2
    print(f"o resultado da adição é: {resultado}")

def subtracao ():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    resultado = num1 - num2
    print(f"o resultado da subtração é: {resultado}")

def multiplicacao ():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    resultado = num1 * num2
    print(f"o resultado da multiplicação é: {resultado}")

def divisao ():
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print(f"o resultado da divisão é: {resultado}")

def pares ():
    limite = int(input("Digite o limite para encontrar números pares: "))
    print(f"Números pares até {limite}:")
    for i in range(2, limite + 1, 2):
        print(i)

def impares ():
    limite = int(input("Digite o limite para encontrar números ímpares: "))
    print(f"Números ímpares até {limite}:")
    for i in range(1, limite + 1, 2):
        print(i)

def somatorio ():
    limite = int(input("Digite o limite para calcular o somatório: "))
    resultado = sum(range(1, limite + 1))
    print(f"O somatório dos números até {limite} é: {resultado}")

def fatorial ():
    num = int(input("Digite um número para calcular o fatorial: "))
    if num == 0:
        print("O fatorial de 0 é 1.")
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        print(f"O fatorial de {num} é: {resultado}")

while True:

    print ("CALCULADORA")
    print ("1 - adição")
    print ("2 - subtração")
    print ("3 - multiplicação")
    print ("4 - divisão")
    print ("5 - pares")
    print ("6 - impares")
    print ("7 - somatorio")
    print ("8 - fatorial")
    print ("0 - sair")

    opcao = input("Escolha uma operação: ")

    if opcao == "1":
        soma()
    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()
    elif opcao == "5":
        pares()
    elif opcao == "6":
        impares()
    elif opcao == "7":
        somatorio()
    elif opcao == "8":
        fatorial()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")