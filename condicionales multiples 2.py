print("============================")
print("Conversor")
print("============================")

print("Menú de opciones")
print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para convertir de palabra a número")

opción= int(input("Cual es tu opción deseada?: "))
if(opción== 1):
    print("Convertir de número a palabra")
    numero= int(input("Ingrese numero que desea convertir a palabra"))
    if(numero==1):
        print("El número es uno")
    elif(numero== 2):
        print("El número es dos")
    elif(numero== 3):
        print("El número es tres")
    elif(numero== 4):
        print("El número es cuatro")
    elif(numero== 5):
        print("El numero es cinco")
    elif(numero== 6):
        print("El número es seis")
    elif(numero== 7):
        print("El número es siete")
    elif(numero== 8):
        print("El número es ocho")
    elif(numero== 9):
        print("El numero es nueve")
    elif(numero== 10):
        print("El número es diez")
    else:
        print("Solo permite hasta el número diez")
elif(opción==2):
    print("Conversor de palabra a número")
    palabra=str(input("Cual es la palabra que desea convertir a número?: "))
    if(palabra== "uno"):
        print("El número es 1")
    elif(palabra== "dos"):
        print("El número es 2")
    elif(palabra== "tres"):
        print("El número es 3")
    elif(palabra== "cuatro"):
        print("El número es 4")
    elif(palabra== "cinco"):
        print("el número es 5")
    elif(palabra== "seis"):
        print("El número es 6")
    elif(palabra== "siete"):
        print("El número es 7")
    elif(palabra== "ocho"):
        print("El número es 8")
    elif(palabra== "nueve"):
        print("el número es 9")
    elif(palabra== "diez"):
        print("el número es 10")
else:
    print("La opción se desconoce")
print("Fin del programa")

