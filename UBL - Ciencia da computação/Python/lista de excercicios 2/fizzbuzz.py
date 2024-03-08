numero = int(input(""))
div3 = numero % 3 
div5 = numero % 5 
if(div3 == 0 and div5 == 0):
        print("FizzBuzz")
else:
        print(numero)