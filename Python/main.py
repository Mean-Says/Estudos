
ODapostado = input("Qual a Od apostada ? ")
ValorApostado = input("Qual o valor apostado ? ")
Contra_Aposta = 0 
OD_contra = input("Qual a Od Contra ? ")

def Apostas(Od, aposta, OD_contra):
    Od = float(ODapostado)
    aposta = float(ValorApostado)
    Od2 = OD_contra
    
    Bet1 = aposta * Od

    for i in range(500):
        Contra_Aposta = i
        Bet2 = Contra_Aposta * Od2
        if Bet2 > Bet1:
            print(Bet2)
            
            break
        else : continue


Apostas(ODapostado, ValorApostado, OD_contra)

input("Pressione Enter para sair...")
input("Pressione Enter para sair...")