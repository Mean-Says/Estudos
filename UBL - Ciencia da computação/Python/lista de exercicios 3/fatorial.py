n = int(input("Digite o valor de n: "))
fatorial = n 
if fatorial == 0:
    fatorial = 1 
    print(fatorial)
else:
    while (n-1) != 0 :
        n = n-1
        fatorial = fatorial * (n)
    print(fatorial)