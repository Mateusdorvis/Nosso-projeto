class Pagamentocinema:
    def __init__(self, pagamento, valor, n_assento, filme, dia, hora):
        self.pagamento = pagamento
        self.valor = valor
        self.n_assento = n_assento 
        self.filme = filme
        self.dia = dia
        self.hora = hora
    
    def gerar_boleto(self, codigo):
        print(f"Tipo de pagamento : {self.pagamento},  código do pagamento : {codigo}, Valor pago : {self.valor}, filme escolhido : {self.filme}, assento escolhido : {self.n_assento},\  dia escolhido : {self.dia}, hora escolhida : {self.hora}")
    
    def cartao_de_credito(self, codigo ):
        print(f"Tipo de pagamento : {self.pagamento}, \ncódigo do pagamento : {codigo}, Valor pago : {self.valor}, filme escolhido : {self.filme}, assento escolhido : {self.n_assento},  dia escolhido : {self.dia}, hora escolhida : {self.hora}")
        
    def pix(self, codigo):
        print(f"Tipo de pagamento : {self.pagamento},  código do pagamento : {codigo}, Valor pago : {self.valor}, filme escolhido : {self.filme}, assento escolhido : {self.n_assento},\  dia escolhido : {self.dia},  hora  escolhida: {self.hora}")
    
    def cartao_de_debito(self, codigo):
        print(f"Tipo de pagamento : {self.pagamento},  código do pagamento : {codigo}, Valor pago : {self.valor}, filme escolhido : {self.filme}, assento escolhido : {self.n_assento}, \ dia escolhido : {self.dia},  hora escolhida : {self.hora}")

#o que está dentro do parametro é argumento para o parametro código



    
        