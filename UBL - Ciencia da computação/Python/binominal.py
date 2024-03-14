def fatorial(x):
    n = x
    if x == 0:
        x = 1
        return x
    else:
        while (n-1) != 0 :
            n = n-1
            x = x * (n)
        return x
    
def binominal(n,p):
    if n >= p: 
        y = fatorial(n)/(fatorial(p)*fatorial(n - p))
        return print(int(y))        
    else: 
        print("Não é possivel pois os valor de N é menor que P")
        return 0
    
n = int(input("Defina o valor de N: "))
p = int(input("Defina o valor de P: "))
binominal(n,p)