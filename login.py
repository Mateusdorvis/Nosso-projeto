
        

def dados_funcionarios(nome: str, senha: int):
    funcionarios = {"Fernanda Farias":123,
                    "Sarah Hassen":456,
                    "Alysson Narciso":789
                    }
    if nome in funcionarios and funcionarios[nome] == senha:
        return True 
    return False
    