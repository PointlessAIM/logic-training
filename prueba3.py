pensum = [
    {'0123': {'creditos': 4,'nombre': 'intro a la ing'}, '4567':{'creditos':1,'nombre':'inglés'}}, 
           {}, 
           {}
           ]
def modificar_materia(pensum,semestre,materia,nombre,creditos):
    
    semestre-=1
    if semestre > len(pensum)-1 or semestre<0:
        mensaje = "Ingrese un semestre válido"
               
    elif len(pensum[semestre]) == 0:
        mensaje = "El semestre no tiene materias"
    elif pensum[semestre].get(materia) == None: 
        mensaje = "La materia no existe"
    else: 
        pensum[semestre][materia] = {'créditos':creditos,'nombre':nombre}
        mensaje = "Modificada con éxito"
    return mensaje

print(modificar_materia(pensum, 4 , '0123' , 'lectoescritura',3))
print(pensum)