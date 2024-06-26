class Pagamentocinema:
    def __init__(self, pagamento, valor, n_assento, filme, dia, hora):
        self.pagamento = pagamento
        self.valor = valor
        self.n_assento = n_assento 
        self.filme = filme
        self.dia = dia
        self.hora = hora
        
    
    def gerar_informacao(self):
        print(f"Tipo de pagamento : {self.pagamento},  código do pagamento : 12345678901 , Valor pago : {self.valor}, filme escolhido : {self.filme}, assento escolhido : {self.n_assento},\  dia escolhido : {self.dia}, hora escolhida : {self.hora}")





    
        