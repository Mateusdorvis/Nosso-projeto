class Assento:
    def __init__(self,nome):
        self.nome = nome
        self.reservado = False
        self.nome_reservado = ""

    def reserva(self,nome):
        self.reservado = True
        self.nome_reservado = nome
    def limpar_reserva(self):
        self.nome_reservado = ""
        self.reservado = False

    def reservado(self):
        self.reservado = True



    





