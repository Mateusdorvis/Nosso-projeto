import login
import catalogo
import main_do_assento

dicionario_filmes = {"filme 1": "Divertida Mente 2", "filme 2": "Os Fantasmas se Divertem 2", "filme 3" : "Guerra Civil", "filme 4": "Duna 2", "filme 5": "A Primeira Profecia", "filme 6": "Bad Boys 4", "filme 7" : 'Um Lugar Silencioso - Dia Um'}

def entrada_funcionario():
    print("Olá!\nInsira seus dados de login para acessar o menu.")

    nome = str(input("Digite seu nome completo: "))
    senha = int(input("Digite sua senha PIN: "))

    if login.dados_funcionarios(nome.upper(), senha):
        ax =""#joga pra algum lugar
    else:
        entrada_funcionario()  
        
def mostrar_menu():
        print("-"*30)
        print("Bem vindo(a) ao nosso sistema")
        print("-"*30)
        print()
        print("O que você deseja fazer agora?")
        print("[1] Ver filmes em cartaz")
        print("[2] Escolher sessão (filme e horário)")
        print("[3] Escolher sala e assento")
        print("[4] Gerar ingresso")
        print()
def main():
     while True:
          mostrar_menu()
          escolha = int(input("Selecione a opção desejada: "))
          
          if escolha == "1":
            print (f"Este é o catalogo de filmes disponiíveis: {dicionario_filmes}")
          elif escolha == "2":
            catalogo.iniciar
            

entrada_funcionario()
mostrar_menu()
main()