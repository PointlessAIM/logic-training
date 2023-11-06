
def funcion (*args):
    # args es una tupla donde pasamos N cantidad de argumentos.
    return print(sum(args)**3)

def funcion2 (**kwargs):
    if 'animal' in kwargs:
        # kwargs['animal'] busca el valor asignado a la llave dentro del diccionario pasado como parámetro.
        print(f"El {'animal'} es un {kwargs['animal']}")
    else:
        print("No hay animal")

# A diferencia de los argumentos pasados a través de variables,
# los args y kwargs no tienen que estar en el mismo orden, ni tienen que ser todos.
# Los args y kwargs son opcionales y no tienen un límite de argumentos.
def funcion3 (*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"Suma de los argumentos: {sum(args)}")
    if 'vehiculo' in kwargs:
        print(f"El {'vehiculo'} es un {kwargs['vehiculo']}")


funcion2(animal='perro', edad=5, nombre='Firulais')
funcion3(15,4,22,1, vehiculo='bicicleta', bebida= 'agua', mascota='tortuga')
funcion(20, 30, 40, 50, 60, 70, 80, 90, 100)

