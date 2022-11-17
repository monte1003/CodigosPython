print("===========")
print("Conversor")
print("===========\n")
print("Menú de opciones\n")
print("Presiona 1 para convertir de número a palabra: ")
print("Presiona 2 para convertir de palabra a número: \n")
parametro= int(input("Ingrese su opción aca: "))
if(parametro==1):
    print("Conversor de número a palabra\n")
    numero= int(input("¿Cúal es el número que deseas convertir a palabra?"))
    if(numero==1):
        print("El número es 'UNO'")
    elif(numero==2):
        print("El número es 'DOS'")
    elif(numero==3):
        print("El número es 'TRES'")
    elif(numero==4):
        print("El número es 'CUATRO'")
    elif(numero==5):
        print("El número es 'CINCO'")
    elif(numero==6):
        print("El número es 'SEIS'")
    elif(numero==7):
        print("El número es 'SIETE'")
    elif(numero==8):
        print("El número es 'OCHO'")
    elif(numero==9):
        print("El número es 'NUEVE'")
    elif(numero==10):
        print("El número es 'DIEZ'")
    else:
        print("El programa solo convierte hasta el numero diez (10)")
elif(parametro==2):
    print("Conversor de palabra a número\n")
    palabra= str(input("¿Cúal es la palabra que deseas convertir a número"))
    palabra= palabra.lower()
    #la función lower nos permite convertir esa cadena de caracteres a minuscula y una vez hecho esto guardarlo dentro de la variable palabra.
    if(palabra== "uno"):
        print("El número es '1'")
    elif(palabra== "dos"):
        print("El número es '2'")
    elif(palabra== "tres"):
         print("El número es '3'")
    elif(palabra== "cuatro"):
        print("El número es '4'")
    elif(palabra== "cinco"): 
        print("El número es '5'")
    elif(palabra== "seis"):
        print("El número es '6'")
    elif(palabra== "siete"):
         print("El número es '7'")
    elif(palabra== "ocho"):
        print("El número es '8'")
    elif(palabra== "nueve"):
        print("El número es '9'")
    elif(palabra== "diez"):
        print("El número es '10'")
    else:
        print("El programa solo convierte hasta el numero diez (10)")
print("Fin del programa.")

    
    

