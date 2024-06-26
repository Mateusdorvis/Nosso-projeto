def escolha_sala():
	print("O filme está dispinível nas seguintes modalidades: \n1. Sala VIP \n2. Sala convencional \n3. Sala IMAX \n4. Sala 3D \n5. Drive-in")
	pergunta3 =int(input("escolha em qual você deseja assistir: "))
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
			return escolha_sala()
escolha_sala()
