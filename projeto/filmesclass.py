class Filme:
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao
    
    def informacao_sobre_filme(self):
        print(f"Titulo do filme : {self.titulo}, Duração : {self.duracao}, Classificacao : +{self.classificacao}")

    def add_favoritos(self, lista):
        questao = int(input(" Deseja a sua lista de favoritos ? 1. Sim 2. Não :"))
        listafav = []
        listafav.append(lista)
        print(listafav)
  #sessao de cinema para + 18
    def verifica_idade_sessao_18(self, idade):
        if idade>=18:
            print("Você pode assistir")
        elif idade<18:
            print("você não pode assistir")
        else: 
            print("invalido")
#sessao de cinema para + 16
    def verifica_idade_sessao_16(self, idade):
        if idade>=16:
            print("Você pode assistir")
        elif idade<16:
            print("você não pode assistir")
        else: 
            print("invalido")
#sessao de cinema para + 14
    def verifica_idade_sessao_14(self, idade):
        if idade>=14:
            print("Você pode assistir")
        elif idade<14:
            print("você não pode assistir")
        else: 
            print("invalido")

#sessao de cinema para + 10
    def verifica_idade_sessao_10(self, idade):
        if idade>=10:
            print("Você pode assistir")
        elif idade<10:
            print("você não pode assistir")
        else: 
            print("invalido")

#sessao de cinema para + 12
    def verifica_idade_sessao_12(self, idade):
        if idade>=12:
            print("Você pode assistir")
        elif idade<12:
            print("você não pode assistir")
        else: 
            print("invalido")
    #sessao de cinema livre
        
        

        