
def gerar_ingresso(filme):

    hora_escolhida= int(input("O cliente deseja para qual horário comercial entre 8h e 22h ?"))

    if hora_escolhida<=22 and hora_escolhida>=8:
        print('ok')

    elif hora_escolhida<8 or hora_escolhida>22:
        print("digite uma hora que seja entre 8h e 22h")
        return gerar_ingresso(filme)
    else:
    	print("invalído")
    	return gerar_ingresso(filme)
    
    minutos = int(input(" O cliente deseja para qual minutos?"))

    
    		



			
   
                
    
        