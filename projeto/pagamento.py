import random

def gerar_ingresso(filme):
    #hora
    hora_escolhida = int(input("Digite o horário desejado (entre 8h a 22h): "))
    if hora_escolhida >=8 and hora_escolhida <=22:
        print("ok")
    
    elif hora_escolhida<8 or hora_escolhida>22:
        print("Digite uma hora entre 8h e 22h.")
        return gerar_ingresso(filme)
       
    else:
        print("invalido")
    #minutos
    minutos = int(input("Digite os minutos desejados (0 a 59): "))
    if minutos <=59 or minutos >=0:
        print("ok")
    
    elif hora_escolhida<8 or hora_escolhida>22:
        print("Digite uma hora entre 8h e 22h.")
        return gerar_ingresso(filme)
    else:
       print("invalido")

    horario = "{}h:{}m".format(hora_escolhida, minutos)
   
    filme_pago = 50
    vip = 100
    convencional = 30
    imax = 50
    trimen = 40
    drive = 32
    bimen = 38
    tipos_de_sessoes = {"sessao 1": " VIP ", "sessao 2": "  convencional  ", "sessao 3" : "  IMAX", "sessao 4": " 3D ", "sessao 5": "  Drive-in", "sessao 6": "2D"}

    questao = int(input('Esta são as sessoes disponiveis : {}, vai escolher querer qual? :'.format(tipos_de_sessoes)))

    if questao==1:
     soma_valor = filme_pago+vip
     sessao_escolhida = tipos_de_sessoes.get("sessao 1")
     print("o cliente escolheu  {} e o valor a ser pago é R$ {}".format(sessao_escolhida,soma_valor))

    elif questao==2:
      soma_valor = filme_pago+convencional
      sessao_escolhida = tipos_de_sessoes.get("sessao 2")
      print("o cliente escolheu  {} e o valor a ser pago é R$ {}".format(sessao_escolhida,soma_valor))

    elif questao==3:
      soma_valor = filme_pago+convencional
      sessao_escolhida = tipos_de_sessoes.get("sessao 3")
      print("o cliente escolheu  {} e o valor a ser pago é R$ {}".format(sessao_escolhida,soma_valor))

    elif questao==4:
      soma_valor = filme_pago+convencional
      sessao_escolhida = tipos_de_sessoes.get("sessao 4")
      print("o cliente escolheu  {} e o valor a ser pago é R$ {}".format(sessao_escolhida,soma_valor))

    elif questao==5:
      soma_valor = filme_pago+convencional
      sessao_escolhida = tipos_de_sessoes.get("sessao 5")
      print("o cliente escolheu  {} e o valor a ser pago é R$ {}".format(sessao_escolhida,soma_valor))

    elif questao==6:
      soma_valor = filme_pago+convencional
      sessao_escolhida = tipos_de_sessoes.get("sessao 6")
      print("o cliente escolheu  {} e o valor a ser pago é R$ {}".format(sessao_escolhida,soma_valor))
    
    else:
       print("invalido")
    
    tipos_de_pagamento = {"Forma de pagamento 1": "Pix", " Forma de pagamento 2": "Cartão de credito ", "Forma de pagamento 3" : " Cartão de débito", "Forma de pagamento 4": "Boleto"}

    questao_pagamento = int(input('Esta são as formas de pagamento disponiveis : {}, vai escolher querer qual? :'.format(tipos_de_pagamento)))

    #codigo aleatorio do valor pago
    code = random.random()

    if questao_pagamento==1:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 1")
      print("o cliente escolheu  {}".format(pagamento_escolhido))

    elif questao_pagamento==2:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 2")
      print("o cliente escolheu  {}".format(pagamento_escolhido))

    elif questao_pagamento==4:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 4")
      print("o cliente escolheu  {}".format(pagamento_escolhido))

    elif questao_pagamento==4:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 1")
      print("o cliente escolheu  {}".format(pagamento_escolhido))
    
    else:
       print("invalido")
    
    print("Tipo de pagamento : {} ,\n codigo do pagamento : {} , \n sessao escolhida :{}, \n filme escolhido : {}, \n hora escolhida : {},\n valor pago : R$ {}".format(pagamento_escolhido, code,sessao_escolhida, filme, horario, soma_valor))
    with open("informacao.txt", "a") as informacao:
    		informacao.write("Tipo de pagamento : {} ,\n codigo do pagamento : {} , \n sessao escolhida :{}, \n filme escolhido : {}, \n hora escolhida : {},\n valor pago : R$ {}".format(pagamento_escolhido, code,sessao_escolhida, filme, horario, soma_valor))
    


