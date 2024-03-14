import math
def baskra(a,b,c):
    delt(a,b,c)
    if (delta > 0):
        print("Com esses parametros o valor de Delta nos da 2 soluções reais diferentes")
        #calcular a raiz quadrada
        x1 = (-b + (math.sqrt(delta)))/ (a * 2)
        x2 = (-b - (math.sqrt(delta)))/ (a * 2)
        #devolver as soluções
        print("e os parametros nos dão essas raises reais:", x1, "e", x2)
    else :
        if (delta == 0):     
            print("Com esses parametros o valor de Delta nos da 2 soluções reais iguais")
            #calcular a raiz quadrada
            x1 = (-b )/ (a * 2)
            x2 = (-b )/ (a * 2)
            #devolver as soluções
            print("e os parametros nos dão essas raises reais:", x1, "e", x2)
        else:
            print("Com esses paremetros, infelizmente não temos uma solução real disponivel")
    return print("")

def delt(a,b,c):
    #calcular delta 
    delta = (b**2) - (4 * a * c)
    return delta

#receber os parametros
a = float(input("Olá para calcular as raizes reais precisamos dos paramentros de a, b e c. Primeiro digite o valor de a: "))
b = float(input("Agora o valor de b: "))
c = float(input("E por ultimo o valor de c: "))

baskra(a,b,c)






        




