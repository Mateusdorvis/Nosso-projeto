class Login:
    def __init__(self, nome_do_user, senha_do_user, data):
        self.nome_do_user = nome_do_user
        self.senha_do_user = senha_do_user
        self.data = data
        
    def __repr__(self):
        return f"Nome o usuario : {self.nome_do_user}, senha do usuario : {self.senha_do_user}, data de nascimento : {self.data}"
        