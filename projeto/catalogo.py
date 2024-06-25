from filmesclass import Filme

filme = Filme("none", 128, 12) #filme é obj
def  iniciar():
	pergunta = int(input("deseja ver catalogo de filmes? 1. Sim , 2.Não :"))
	if pergunta==1:
		def filmes():
			dicionario_filmes = {"filme 1": "Duna 2", "filme 2": "Divertida Mente 2", "filme 3" : "Os Fantasmas se divertem 2", "filme 4" : "O coringa 2"}
			pergunta2 = int(input(f'Este é o catalogo de filmes disponivel : {dicionario_filmes}, vai escolher querer qual? '))
			match pergunta2:
				case 1:
					filme1 = dicionario_filmes.get("filme 1")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 128, 12)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_12(anos)
					

				case 2:
					filme1 = dicionario_filmes.get("filme 2")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 128, "L")
					filme.informacao_sobre_filme()

				case 3:
					filme1 = dicionario_filmes.get("filme 3")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 128, 12)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_12(anos)
				case 4:
					filme1 = dicionario_filmes.get("filme 4")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 128, 16)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_12(anos)
				case _:
					print("invalido")
		filmes()

	elif pergunta==2:
		print("ok obrigado")
	else:
		print("digite um número")
		return iniciar()
iniciar()

