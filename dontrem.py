#si el promedio está entre 0 y 20 -> grupo 1
#si el promedio está entre 21 y 40 -> grupo 2
#si el promedio está entre 41 y 70 -> grupo 3
#si el promedio está encima de 70 -> grupo 4
#calcular el promedio de Hugo, Paco y Luis
#Dado el promedio de Hugo, calcular los promedios de Paco y Luis separados por espacio
#En una segunda linea, mostrar el grupo al que pertenece el promedio de Luis


#String = "Hola, como estas?"
#char = un caracter de la cadena
#boolean = True or False
#int = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 
#long = 1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L, 9L, 10L
#float = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0
#double = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0

promedio_Hugo = eval(input("Ingrese el promedio de Hugo: "))
promedio_Hugo = int(promedio_Hugo)
promedio_Paco = int((promedio_Hugo*2)+4)
promedio_Luis = int((promedio_Hugo+promedio_Paco)/2)


print (promedio_Paco," ", promedio_Luis," ", promedio_Hugo)

if promedio_Luis >= 0 and promedio_Luis <= 20:
    print ("El promedio de Luis esta en el grupo 1")
elif promedio_Luis >= 21 and promedio_Luis <= 40:
    print ("El promedio de Luis esta en el grupo 2")
elif promedio_Luis >= 41 and promedio_Luis <= 70:
    print ("El promedio de Luis esta en el grupo 3")
else:
    print ("El promedio de Luis esta en el grupo 4")


 
