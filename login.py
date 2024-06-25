class Funcionario:
    def __init__ (self, nome: str, senha: int):
        self.nome = nome
        self.senha = senha
    def __repr__(self):
        return f"pessoa(nome='{self.nome}', senha ={self.senha})"
    
pessoa1 = Funcionario("Fernanda Farias", 123)
pessoa2 = Funcionario("Sarah Hassen", 456)
pessoa3 = Funcionario("Alysson Narciso", 789)

lista_funcionarios = [pessoa1, pessoa2, pessoa3]

def dados_funcionarios(nome: str, senha: int):  
    funcionarios = [pessoa1,pessoa2,pessoa3]
    auxiliar = False
    for funcionario in funcionarios:
        if nome.upper() == funcionario.nome.upper() and senha == funcionario.senha:
            auxiliar = True 
            break
        else:
            auxiliar = False
    if auxiliar:
        print("Acesso liberado!")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False
    
       