SegundosTotal = int(input("Por favor, entre com o número de segundos que deseja converter: "))

DiasTotal = (SegundosTotal // 3600) // 24
HorasTotal = (SegundosTotal // 3600) % 24
SegundosTotal = SegundosTotal % 3600
MinutosTotal = SegundosTotal // 60
SegundosTotal = SegundosTotal % 60

print(DiasTotal, "dias,", HorasTotal,"horas,",MinutosTotal,"minutos e",SegundosTotal,"Segundos")    

