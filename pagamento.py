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
        return gerar_ingresso(filme)
    
    #minutos
    minutos = int(input("Digite os minutos desejados (0 a 59): "))
    if minutos <=59 or minutos >=0:
        print("ok")
    
    elif hora_escolhida<8 or hora_escolhida>22:
        print("Digite uma hora entre 8h e 22h.")
        return gerar_ingresso(filme)
    else:
       print("invalido")
       return gerar_ingresso(filme)

    horario = "{}h:{}m".format(hora_escolhida, minutos)

     #dia
    dia = int(input("Digite o dia ENTRE 1 A 31: "))
    numero_mes = int(input("Digite o numero de mes (EX) 1. JAN ,  2. FEV,  3.MAR,  4.ABR,  5.MAI,  6.JUN,  7. JUL,  8.AGO,  9.SET,  10.OUT ,  11.NOV ,  12.DEZ :"))
    if numero_mes >=1 and numero_mes<=12:
       print("ok")
    elif numero_mes<1 or numero_mes>12:
       print("invalido")
       return gerar_ingresso(filme)
    else: 
       print("invalido")
       return gerar_ingresso(filme)
    
    ano_desejado = int(input("Digite o ano :"))

    dta_completa = "{} / {} / {}".format(dia, numero_mes, ano_desejado)

    #sessao mais valor
    filme_pago = 50 #valor de cada filme
    #valor de cada sessao do cinema
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

    #forma de como o cliente vai pagar
    tipos_de_pagamento = {"Forma de pagamento 1": "Pix", " Forma de pagamento 2": "Cartão de credito ", "Forma de pagamento 3" : " Cartão de débito", "Forma de pagamento 4": "Boleto"}

    questao_pagamento = int(input('Esta são as formas de pagamento disponiveis : {}, vai escolher querer qual? :'.format(tipos_de_pagamento)))

    if questao_pagamento==1:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 1")
      print("o cliente escolheu como forma de pagamento :  {}".format(pagamento_escolhido))

    elif questao_pagamento==2:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 2")
      print("o cliente escolheu  como forma de pagamento : {}".format(pagamento_escolhido))

    elif questao_pagamento==4:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 4")
      print("o cliente escolheu  como forma de pagamento : {}".format(pagamento_escolhido))

    elif questao_pagamento==4:
      pagamento_escolhido = tipos_de_pagamento.get("Forma de pagamento 1")
      print("o cliente escolheu  como forma de pagamento : {}".format(pagamento_escolhido))

    else:
       print("invalido")

     #codigo aletorio do valor a ser pago 
    code = random.random()

    #exibindo a informação coletada na tela
    print("Tipo de pagamento : {} ,\n codigo do pagamento : {} , \n sessao escolhida :{}, \n filme escolhido : {}, \n hora escolhida : {},\n valor  a ser pago : R$ {}, \n data escolhida para o ver o filme : {} ".format(pagamento_escolhido, code,sessao_escolhida, filme, horario, soma_valor, dta_completa))
    #salavndo informação
    with open("ingresso.txt", "a") as informacao:
    		informacao.write("Tipo de pagamento : {} ,\n codigo do pagamento : {} , \n sessao escolhida :{}, \n filme escolhido : {}, \n hora escolhida : {},\n valor  a ser pago : R$ {}, \n data escolhida para o ver o filme : {} ".format(pagamento_escolhido, code,sessao_escolhida, filme, horario, soma_valor, dta_completa))
    


