def repetir(texto,rep):
    texto += '\n'
    print(texto*rep)

t = input("Ingrese texto a imprimir: ")
r = int(input("Ingrese el numero de veces que se va a imprimir el texto: "))
repetir(t,r)