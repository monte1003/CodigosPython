
print("Calculadora con una sola variable\n")
print("Menú de opciones\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Potenciación")
print("7. Modulo o resto\n")
numero= int(input("¿Cual es la operación que desea ejecutar?"))
if(numero==1):
    print("Escogiste la suma")
    numero= int(input("Ingrese el primer número"))
    numero+=int(input("Ingrese el segundo número"))
    print("El resultado de la suma es", numero)
elif(numero==2):
    print("Escogiste resta")
    numero= int(input("Ingrese el primer número"))
    numero-=int(input("Ingrese el segundo número"))
    print("El resultado de la resta es", numero)
elif(numero==3):
    print("Escogiste Multiplicación")
    numero= int(input("Ingese el primer número"))
    numero*=int(input("Ingrese el segundo número"))
    print("El resultado de la multiplicación es", numero)
elif(numero==4):
    print("Escogiste División")
    numero=float(input("Ingrese el dividendo"))
    numero/=float(input("Ingrese el divisor"))
    print("El resultado de la división es", round(numero,2))
elif(numero==5):
    print("Escogiste Divisón entera")
    numero= int(input("Ingrese el primer número"))
    numero//= int(input("Ingrese el segundo número"))
    print("El resultado de la división entera es", numero)
elif(numero==6):
    print("Escogise potenciación")
    numero= int(input("Ingrese la base"))
    numero**= int(input("Ingrese el exponente"))
    print("El resultado de la potenciación es", numero)
elif(numero==7):
    print("Escogiste Modulo o resto")
    numero= int(input("Ingrese el primer número"))
    numero%= int(input("Ingrese el segundo número"))
    print("El resultado del modulo o resto es", numero)
else:
    print("Opción no disponible\n")
print("Fin del programa.")




