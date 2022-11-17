#Operadores relaciones python
#Conjunción



print("Ejercicio de conjunción\n")
numero= int(input("Introduce un número mayor que 2 y menor que 6"))
if(numero>2 and numero<6 ):
    print("El número cumple con la condición\n")
else:
    print("El número NO cumple con la condición\n")

#Disyunción
print("Ejercicio de disyunción\n")
palabra= str(input("Para cumplir con la condición introduza la palabra 'si' o 'yes'\n"))
if (palabra== "si" or "yes"):
    print("Se cumple la condición\n")
else:
    print("No se cumple la condición\n")

#Negación
print("Ejericio de negación (negar la condición)")
cinco= int(input("Introduce el número 5"))