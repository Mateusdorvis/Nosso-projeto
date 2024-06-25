
def escolhas():
	pergunta3 =int(input("A seguir escolha qual tipo de sala que queira : 1. Sala VIP, 2. Sala convencional, 3. Sala IMAX, 4.Sala 3D, 5. drive-in :"))
	match pergunta3:
		case 1:
			print("vc escolheu sala vip")
		case 2:
			print("vc escolheu sala convencional")
		case 3:
			print("vc escolheu sala imax")
		case 4:
			print("vc escolheu sala 3d")
		case 5:
			print("vc escolheu para drive-in")
		case _:
			print("inválido")
			return escolhas()
escolhas()
