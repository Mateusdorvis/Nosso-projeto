
def escolhas():
	escolhasala = {"Forma de pagamento 1": "Sala VIP", "Forma de pagamento 2": "Sala convencional", "Forma de pagamento 3" : "Sala 3D,", "Forma de pagamento  4": "drive-in","Forma de pagamento  5": "Sala IMAX" }
	
	pergunta3 =int(input(f"A seguir escolha qual tipo de sala que queira : {tipopagamento} "))
	
	if pergunta3==1:
			tira = escolhasala.get("Forma de pagamento 1")
			print(f"vc escolheu {tira} ")
	elif pergunta3==2:
			tira = escolhasala.get("Forma de pagamento 2")
			print(f"vc escolheu  {tira}")
	elif pergunta3==3:
			tira = escolhasala.get("Forma de pagamento 3")
			print(f"vc escolheu {tira} ")
	elif pergunta3==4:
			tira = escolhasala.get("Forma de pagamento 4")
			print(f"vc escolheu {tira} ")
	elif pergunta3==5:
			tira = escolhasala.get("Forma de pagamento 5")
			print(f"vc escolheu  {tira} ")
	else:
			print("inválido")
			return escolhas()
escolhas()
