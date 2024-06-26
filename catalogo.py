from filmesclass import Filme
import escolhas

filme = Filme("none", 128, 12) #filme é obj
def  iniciar():
		def filmes():
			dicionario_filmes = {"filme 1": "Divertida Mente 2", "filme 2": "Os Fantasmas se Divertem 2", "filme 3" : "Guerra Civil", "filme 4": "Duna 2", "filme 5": "A Primeira Profecia", "filme 6": "Bad Boys 4", "filme 7" : 'Um Lugar Silencioso - Dia Um'}
			pergunta2 = int(input(f'Este é o catalogo de filmes disponivel : {dicionario_filmes}, qual a escolha ? '))
			match pergunta2:
				case 1:
					filme1 = dicionario_filmes.get("filme 1")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 96, 10)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_10(anos)
					filme.add_favoritos(filme1)

				case 2:
					filme1 = dicionario_filmes.get("filme 2")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 148, 12)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_12(anos)
					filme.add_favoritos(filme1)

				case 3:
					filme1 = dicionario_filmes.get("filme 3")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 110, 18)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_18(anos)
					filme.add_favoritos(filme1)

				case 4:
					filme1 = dicionario_filmes.get("filme 4")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 176, 12)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_12(anos)
					filme.add_favoritos()

				case 5:
					filme1 = dicionario_filmes.get("filme 5")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 117, 12)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_12(anos)
					filme.add_favoritos()

				case 6:
					filme1 = dicionario_filmes.get("filme 6")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 105, 14)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_14(anos)
					filme.add_favoritos(filme1)

				case 7:
					filme1 = dicionario_filmes.get("filme 7")
					print(f"você quer assistir {filme1}")
					filme = Filme(filme1, 100, 16)
					filme.informacao_sobre_filme()
					anos = int(input("Tem quantos anos :"))
					filme.verifica_idade_sessao_16(anos)
					filme.add_favoritos(filme1)
				case _:
					print("invalido")

iniciar()