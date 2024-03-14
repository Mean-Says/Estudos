def maior_primo(n):
    i = 1
    Soma_de_divisores = 0
    while i < n:
        i += 1
        consulta = n % i 
        if consulta == 0: 
            Soma_de_divisores = Soma_de_divisores + i
        else:
            i = i + 1
    return 
            
maior_primo(200)
print("teste")