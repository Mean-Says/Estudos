numero = int(input("Digite o numero que vai ser somado "))
y = 0
soma = 0
while numero != 0 :

    y = numero % 10
    numero = (numero) // 10
    soma = soma + y 

print("A soma dos numeros é", soma)


    