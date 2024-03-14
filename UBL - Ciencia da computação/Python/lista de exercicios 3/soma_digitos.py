numero = int(input("Digite um número inteiro: "))
y = 0
soma = 0
while numero != 0 :
    y = numero % 10
    numero = (numero) // 10
    soma = soma + y 
print(soma)


    