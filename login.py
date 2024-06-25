"""class Login:
    def __init__(self, nome_do_user, senha_do_user, data, cpf):
        self.nome_do_user = nome_do_user
        self.senha_do_user = senha_do_user
        self.data = data
        self.cpf = cpf

    def exibir(self):
        print(f"Nome o usuario : {self.nome_do_user}, senha do usuario : {self.senha_do_user}, data de nascimento : {self.data}, CPF : {self.cpf}")

pergunta1 = input(" nome do user :")
pergunta2 = input("senha do user")
pergunta3 = int(input("data de nascimento :"))
pergunta4 = int(input("cpf :"))
login = Login(pergunta1, pergunta2, pergunta3, pergunta4)
login.exibir()"""
        

def dados_funcionarios(nome: str, senha: int):
    funcionarios = {"Fernanda Farias":123,
                    "Sarah Hassen":456,
                    "Alysson Narciso":789
                    }
    if nome in funcionarios and funcionarios[nome] == senha:
        return True 
    return False
    