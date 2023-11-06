'''
con la estructura try: ... except: ... else: ... finally: ... podemos validar 
pedazos de código que podrían devolver un error y de esta forma, ser nosotros
quienes lo manejemos. 

try: podemos verlo como crear un entorno controlado para probar si el código 
    funciona correctamente.
except: en el caso de que algo vaya mal con lo de arriba, esto nos deja manejar
    el error, usualmente enviando una alerta o retornando un mensaje de error.
else: lo usamos cuando queremos hacer algo con el código después de comprobar que
    no hay error, los siguientes pasos.
finally: aquí ejecutamos el código que queremos sin importar lo que pasó previamente
    un buen ejemplo de esto es cuando lidiamos con archivos y luego de todo el proceso
    necesitamos cerrarlo, ese código de cierre iría en este bloque.
'''
try:
    resultado = 10 + '10'
    print (resultado)

except:
    print("Ha ocurrido un error, escriba correctamente las variables")

finally:
    print ("Gracias, vuelva pronto!")