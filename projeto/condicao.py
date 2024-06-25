def cinema():
	dicio_filmes_disponiveis = {"filme 1": "Divertida Mente 2", "filme 2": "Os Fantasmas se Divertem 2", "filme 3" : "Guerra Civil", "filme 4": "Duna 2", "filme 5": "A Primeira Profecia", "filme 6": "Bad Boys 4", "filme 7" : 'Um Lugar Silencioso - Dia Um'}
	print("Este é o catalogo disponivel : {}".format(dicio_filmes_disponiveis))
	pergunta2 = int(input("Dos filmes de 1 a 7 disponiveis vai querer qual? : "))
	if pergunta2==1:
		transformar = dicio_filmes_disponiveis.get("filme 1")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	elif pergunta2==2:
		transformar = dicio_filmes_disponiveis.get("filme 2")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	elif pergunta2==3:
		transformar = dicio_filmes_disponiveis.get("filme 3")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	elif pergunta2==4:
		transformar = dicio_filmes_disponiveis.get("filme 4")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	elif pergunta2==5:
		transformar = dicio_filmes_disponiveis.get("filme 5")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	elif pergunta2==6:
		transformar = dicio_filmes_disponiveis.get("filme 6")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	elif pergunta2==7:
		transformar = dicio_filmes_disponiveis.get("filme 7")
		print("você quer assistir : {}".format(transformar))
		sim_nao = int(input("Tem certeza que quer assistir este filme ? Digite 1.Sim para assistir 2. Não assistir :"))
		if sim_nao==1:
				print("Vamos prosseguir o processo...")
		elif sim_nao==2:
				print("oK, retornaremos o catalogo disponível")
				return cinema()
		else:
				print("invalido, digite um número")
				return cinema()
	else:
		print("invalido, digite um número por favor ")
		return cinema()
cinema()
