numero1 = int(input("Ingresa numero de inicio : "))
numero2 = int(input("Ingresa ultimo numero: "))
suma = 0
for numero in range(numero1 ,numero2 +1):
    suma += numero

print(suma)