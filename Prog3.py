num1 = int(input("Ingrese primer numero"))
num2 = int(input("Ingrese segundo numero"))


print("Menu")
print("Operaciones: ")
print("S. Suma")
print("R. Resta") 
print("M. Mutiplicacion")
print("D. Division")
print("A. Salir")
opcion = int(input("¿Que opcion eliges?")

if opcion.upper() == "S":
    result = num1 + num2
    print(result)

elif opcion.upper() == "R":
    result = num1 - num2
    print(result)

elif opcion.upper() == "M":
    result = num1 * num2
    print(result)

elif opcion.upper() == "D":
    result = num1/num2
    print(result)

elif opcion.upper() == "A"
    brake