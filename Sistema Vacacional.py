print("Sistema para determinar días de vacaciones para los empleados de rappi\n")
nombre= str(input("Ingrese el nombre del empleado"))
print("Presione 1 si el empleado pertenece al departamento de atención al cliente")
print("Presione 2 si el empleado peretence al departamento de logística")
print("Presione 3 si el empleado pertenece a la gerencia\n")
depto= int(input("Introduce la clave del departamento"))
if(depto==1):
    años= int(input("Introduce tus años de servicio en la empresa"))
    if(años==1):
        print("El empleado",nombre, "tiene derecho a 6 días de vacaciones")
    elif(años>=2 and años<=6):
        print("El empleado", nombre, "tiene derecho a 14 días de vacaciones")
    elif(años>=7):
        print("El empleado", nombre, "tiene derecho a 30 días de vacaciones")
elif(depto==2):
    años2= int(input("Introduce tus años de servicio en la empresa"))
    if(años2==1):
        print("El empleado", nombre, "tiene derecho a 7 días de vacaciones")
    elif(años2>=2 and años2<=6):
        print("El empleado ", nombre, "tiene derecho a 15 días de vacaciones")
    elif(años2>=7):
        print("El empleado ", nombre, "tiene derecho a 22 días de vacaciones")
elif(depto==3):
    años3= int(input("Introduce tus años de servicio en la empresa"))
    if(años3==1):
        print("El empleado", nombre, "tiene derecho a 10 días de vacaciones")
    elif(años3>=2 and años3<=6):
        print("El empleado", nombre, "tiene derecho a 20 días de vacaciones")
    elif(años3>=7):
        print("El empleado", nombre, "tiene derecho a 30 días de vacaciones")
else:
    print("La clave del departamento no existe")
print("Fin del programa.")

