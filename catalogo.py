from filmesclass import Filme
import pagamento
filme = Filme("none", 128, 12)

#funcao
def  iniciar():
	dicionario_filmes = {"filme 1": "Divertida Mente 2", "filme 2": "Os Fantasmas se Divertem : Beetlejuice", "filme 3" : "Guerra Civil", "filme 4": "Duna 2", "filme 5": "A Primeira Profecia", "filme 6": "Bad Boys 4", "filme 7" : 'Um Lugar Silencioso - Dia Um'}
	pergunta2 = int(input('Este é o catalogo de filmes disponivel : {}, vai escolher querer qual? :'.format(dicionario_filmes)))
	#se cai na condição 1
	if pergunta2==1:
		tirar_valor_chave = dicionario_filmes.get("filme 1")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 128, 10)
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.verifica_idade_sessao_10(anos)
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)

	#se cair na condiçao 2
	elif pergunta2==2:
		tirar_valor_chave = dicionario_filmes.get("filme 2")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 134, "L")
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)
	#condicao 3
	elif pergunta2==3:
		tirar_valor_chave = dicionario_filmes.get("filme 3")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 128, 16)
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.verifica_idade_sessao_16(anos)
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)
	#condicao 4
	elif pergunta2==4:
		tirar_valor_chave = dicionario_filmes.get("filme 4")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 128, 14)
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.verifica_idade_sessao_14(anos)
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)
	#condicao 5
	elif pergunta2==5:
		tirar_valor_chave = dicionario_filmes.get("filme 5")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 128, 18)
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.verifica_idade_sessao_18(anos)
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)
	#condicao 6
	elif pergunta2==6:
		tirar_valor_chave = dicionario_filmes.get("filme 6")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 128, 16)
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.verifica_idade_sessao_16(anos)
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)
	#condicao 7
	elif pergunta2==7:
		tirar_valor_chave = dicionario_filmes.get("filme 7")
		print("você quer assistir {}".format(tirar_valor_chave))
		filme = Filme(tirar_valor_chave, 60, 16)
		filme.informacao_sobre_filme()
		anos = int(input(" o cliente tem quantos anos :"))
		filme.verifica_idade_sessao_16(anos)
		filme.add_favoritos(tirar_valor_chave)
		pagamento.gerar_ingresso(tirar_valor_chave)
iniciar()

