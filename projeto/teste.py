from pagamento import Pagamentocinema

def data_hora():
    hora = int(input("digite um horário entre 8h e 22h:"))
    if hora>=22:
        print("digite um horário menor que 22h")
    elif hora<=8:
          print("digite um horário maior que 8h")
    else:
        print("ok")
        
    minutos = int(input("digite a hora que seja entre 0 a 59 minutos:"))
    if minutos>=60:
        print("digite um minuto que seja menor que 60 minutos:")
    else:
        print("ok")
        
    dia = int(input("digite o dia :"))
    if dia>=31:
        print("digite um dia certo")
    else:
        print("ok")
        
    numero_mes =  dia = int(input("digite o numero do mês ex para ajudar 1. JAN, 2. FEV, 3. MAR, 4.ABR , 5. MAI,6.JUN, 7.JUL , 8.AGO, 9.SET, 10 OUT, 11. NOV, 12. DEZ:"))
    if numero_mes>=31:
        print("digite um dia certo")
    else:
        print("ok")
        
    ano = int(input("digite o ano :"))
    if ano==" ":
        print("digite um dia certo")
    else:
        print("ok")
    
    hora_completa = f"{hora} h : {minutos} m"
    dia_completo = f"{dia} / {numero_mes} / {ano}"
data_hora()

