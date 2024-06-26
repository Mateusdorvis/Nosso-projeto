
def escolhas():
	escolhasala = {"Escolha de sala 1": "Sala VIP", "Escolha de sala  2": "Sala convencional", "Escolha de sala 3" : "Sala 3D,", "Escolha de sala  4": "drive-in","Escolha de sala  5": "Sala IMAX" }
	
	pergunta3 =int(input(f"A seguir escolha qual tipo de sala que queira : {escolhasala} "))
	
	if pergunta3==1:
			tira = escolhasala.get("Escolha de sala 1")
			print(f"vc escolheu {tira} ")
	elif pergunta3==2:
			tira = escolhasala.get("Escolha de sala 2")
			print(f"vc escolheu  {tira}")
	elif pergunta3==3:
			tira = escolhasala.get("Escolha de sala 3")
			print(f"vc escolheu {tira} ")
	elif pergunta3==4:
			tira = escolhasala.get("Escolha de sala 4")
			print(f"vc escolheu {tira} ")
	elif pergunta3==5:
			tira = escolhasala.get("Escolha de sala 5")
			print(f"vc escolheu  {tira} ")
	else:
			print("inválido")
			return escolhas()
escolhas()
