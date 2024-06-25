import login
from assento import Assento

"""class entrada_funcionario:
   print("Insira seus dados de login para continuar")
nome = input("Digite seu nome completo: ")
senha = int(input("Digite sua senha PIN: "))

if not login.dados_funcionarios(nome,senha):
   print("Nome de usuário ou senha incorretos.")
    
else:
   print("Acesso liberado!")"""
def reserva_assento():
    fileiraA = [Assento('A1'),Assento("A2"),Assento('A3'),Assento('A4'),Assento('A5'),Assento('A6'),Assento('A7'),Assento('A8')]
    for assento in fileiraA:
        print(f'Assento: {assento.nome} status reservado: {assento.reservado} nome da reserva: {assento.nome_reservado}')
    escolha = input("escolha um assento disponível").upper
    match escolha:
        case 'A1':
            if assento[0].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[0].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case 'A2':
            if assento[1].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[1].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case 'A3':
            if assento[2].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[2].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case 'A4':
            if assento[3].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[3].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case  'A5':
            if assento[4].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[4].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case 'A6':
            if assento[5].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[5].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case 'A7':
            if assento[6].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[6].reserva(nome)
            print("Lugar Reservado com sucesso!")

        case 'A8':
            if assento[7].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite seu nome: ")
            fileiraA[7].reserva(nome)
            print("Lugar Reservado com sucesso!")
        
        
            
        

               

        


