menu = "0"
while menu == "0":
    opcion = input("¿Que opcion eliges?: ").upper()
    print("Menu")
    print("Operaciones: ")
    print("S. Suma")
    print("R. Resta") 
    print("M. Mutiplicacion")
    print("D. Division")
    print("A. Salir")
   
    num1 = int(input("Ingrese primer numero"))
    num2 = int(input("Ingrese segundo numero"))


    if opcion == "S":
        result = num1 + num2
        print(result)

    elif opcion == "R":
        result = num1 - num2
        print(result)

    elif opcion == "M":
        result = num1 * num2
        print(result)

    elif opcion == "D":
        result = num1/num2
        print(result)

    elif opcion == "A":
        print("Saliendo del programa")
        break
