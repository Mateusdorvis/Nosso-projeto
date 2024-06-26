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

    def tipopagamento():
        escolhapagamento = {"Forma de pagamento 1": "Pix", "Forma de pagamento 2": "Cartão de crédito", "Forma de pagamento 3" : "Cartão de débito", "Forma de pagamento  4": "Boleto" }
        paga =int(input(f"A seguir escolha qual tipo de sala que queira : {escolhapagamento} "))
        if paga==1:
            tira2 = escolhapagamento.get("Forma de pagamento 1")
            print(f"você escolheu como forma de pagamento via {tira2}")
        elif paga==2:
            tira2 = escolhapagamento.get("Forma de pagamento 2")
            print(f"você escolheu como forma de pagamento via {tira2}")
        elif paga==3:
            tira2 = escolhapagamento.get("Forma de pagamento 3")
            print(f"você escolheu como forma de pagamento via {tira2}")
        elif paga==4:
            tira2 = escolhapagamento.get("Forma de pagamento 4")
            print(f"você escolheu como forma de pagamento via {tira2}")



    
        