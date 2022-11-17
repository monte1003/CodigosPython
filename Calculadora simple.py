print("Bienvenido a la calculadora simple")
parametro= str(input(" Ingrese que operación quiere realizar "))
numero_uno= int(input("Ingrese un número"))
numero_dos= int(input(" Ingrese el otro número "))
if(parametro=="suma" ):
   resultado_suma= numero_uno + numero_dos
   print("El resultado de la suma ", resultado_suma)
elif(parametro== "resta"):
    resultado_resta= numero_uno - numero_dos
    print("El resultado de la resta es ", resultado_resta)
elif(parametro=="multiplicacion"):
    resultado_multiplicacion= numero_uno*numero_dos
    print("el resultado de la multiplicación es ", resultado_multiplicacion)
elif(parametro=="division"):
    resultado_division= numero_uno//numero_dos
    print("El resultado de la división es ", resultado_division)
elif(parametro== "potenciacion"):
    resultado_potenciacion= numero_uno**numero_dos
    print("El resultado de la potencia es ", resultado_potenciacion)
elif(parametro== "radicacion"):
    from math import sqrt
    resultado_radicacion1= sqrt(numero_uno)
    resultado_radicacion2= sqrt(numero_dos)
    print("La raíz cuadrada del primer número es ", resultado_radicacion1, "y la raíz cuadrada del segundo número es ", resultado_radicacion2)


else:
    print("Opción no disponible")
print("Fin del programa")