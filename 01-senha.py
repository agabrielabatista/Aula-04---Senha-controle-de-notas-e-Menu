nome = input("digite o nome ")
senha_digitada = input("digite a senha ")
senha_cadastrada = '123'

while senha_digitada != senha_cadastrada:
    print("senha incorreta! tente novamente")
    senha_digitada = input("digite sua senha:")
    
print (f"{nome}, bem-vindo ao sistema...")