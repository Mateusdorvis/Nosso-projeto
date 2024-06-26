class Pagamentocinema:
    
    def __init__(self, pagamento, valor, n_assento, filme, dia, hora):
        self.pagamento = pagamento
        self.valor = valor
        self.n_assento = n_assento 
        self.filme = filme
        self.dia = dia
        self.hora = hora
        
    
    def gerar_contaprapagar(self):
        codigo_padrao = 12345678901
        print(f"Tipo de pagamento : {self.pagamento},  código do pagamento : {codigo_padrao}, Valor pago : {self.valor}, filme escolhido : {self.filme}, assento escolhido : {self.n_assento},\  dia escolhido : {self.dia}, hora escolhida : {self.hora}")

    def tipopagamento(self):
        escol = {"Forma de pagamento 1": "Sala VIP", "Forma de pagamento 2": "Sala convencional", "Forma de pagamento 3" : "Sala 3D,", "Forma de pagamento  4": "drive-in","Forma de pagamento  5": "Sala IMAX" }
        pergunta =int(input(f"A seguir escolha qual tipo de sala que queira : {escolhasala} "))
	


#o que está dentro do parametro é argumento para o parametro código



    
        