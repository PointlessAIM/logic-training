
nombre = 'global'

def outer():
    global nombre 
    print (nombre)
    nombre = 'outer'
    def inner():
        nombre = 'inner'
        print(nombre)
    inner()
    print(nombre)
    

outer()
