import login

def entrada_funcionario():
    print("Insira seus dados de login para continuar")

    nome = str(input("Digite seu nome completo: "))
    senha = int(input("Digite sua senha PIN: "))

    if login.dados_funcionarios(nome.upper(), senha):
        ax =""#joga pra algum lugar
    else:
        entrada_funcionario()    
        
entrada_funcionario()
  


