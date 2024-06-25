import login

class entrada_funcionario:
   print("Insira seus dados de login para continuar")
nome = input("Digite seu nome completo: ")
senha = int(input("Digite sua senha PIN: "))

if not login.dados_funcionarios(nome,senha):
   print("Nome de usuário ou senha incorretos.")
    
else:
   print("Acesso liberado!")

    

