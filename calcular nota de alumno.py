print("Sistema para calcular promedio de un alumno")
nombre= input("Para comenzar, introduce tu nombre y apellido  ")
matematicas= float(input(nombre + " introduce tu nota final de matemáticas "))
biologia= float(input(nombre + " introduce tu nota final de biología "))
español= float(input(nombre + " introduce tu nota final de  español "))
informatica= float(input(nombre + " introduce tu nota final de informatica "))
eduación_física= float(input(nombre + " introduce tu nota final de educación física"))
química= float(input(nombre + " introduce tu nota final de química "))
geometría= float(input(nombre + " introduce tu nota final de geometría"))
comp_ciudadana= float(input(nombre +" introduce tu nota final de competencia ciudadana"))
c_lectora= float(input(nombre + " introduce tu nota final de comprensión lectora"))
música= float(input (nombre + " introduce tu nota final de musica"))
emprendimiento= float(input(nombre + " introduce tu nota final de emprendimiento"))
artística= float(input(nombre + " introduce tu nota final de artística"))
sociales= float(input(nombre + " introduce tu nota final de sociales"))
ingles= float(input(nombre + " introduce tu nota final de ingles"))
estadística= float(input(nombre + " introduce tu nota final de estadística"))
física= float(input(nombre + " introduce tu nota final de física"))
proyecto_de_vida= float(input(nombre + " introduce tu nota final de proyecto de vida"))
lectura_crítica= float(input(nombre + " introduce tu nota final de lectura crítica"))
etica= float(input(nombre + " introduce tu nota final de etica"))
educación_cristiana= float(input(nombre + " ingresa tu nota final de educación cristiana"))





promedio= (matematicas + biologia + español + informatica + eduación_física + química + geometría +comp_ciudadana + c_lectora + música + emprendimiento + artística + sociales + ingles + estadística + física + proyecto_de_vida + lectura_crítica + etica + educación_cristiana)/20

if promedio >= 3.5:
    print("Felicidades  " + nombre +  " aprobaste con un promedio de: " , round(promedio, 1))
else :
    print("Lo sentimos " + nombre + " reprobaste con un promedio de " , round(promedio, 1))

print("FIN DEL PROGRAMA")

