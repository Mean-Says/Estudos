numero = int(input("Digite um numero: "))
adjacente = False 
while numero != 0 : 
    x = numero % 10
    numero =  numero // 10
    y = numero % 10
    if x == y:
        adjacente = True

if adjacente == True: 
    print("esse numero tem adjacentes iguais ")
else: 
    print("Este numero não tem adjancentes iguais")

    