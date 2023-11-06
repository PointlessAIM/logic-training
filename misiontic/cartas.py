
baraja= ('Q', '6', '7', '4', 'K', '4', '4', '2', '3', '6', '10', 'Q', '6', 
'3', '10', 'K', '8', '9', 'J', 'J', '9', '9', '2', 'A', 'K', '5', 
'J', '2', 'K', '8', 'A', '5', 'Q', '5', '5', '4', '3', '3', '8', 
'9', '8', '6', '7', 'Q', 'A', '7', '2', '10', '7', 'A', 'J', '10')


def tiene_cartas_altas(cartas_siguientes):
    
    cartas_altas = False
    
    if "A" in cartas_siguientes:
        cartas_altas = True
    if "J" in cartas_siguientes:
        cartas_altas = True
    if "Q" in cartas_siguientes:
        cartas_altas = True
    if "K" in cartas_siguientes: 
        cartas_altas = True
    
    return cartas_altas

def juego(baraja): 
    
    jugador_uno = 0
    jugador_dos = 0
    temp = 0
    count = 0

    for i in baraja:
        
        barajas_restantes = len (baraja) - (count + 1)

        if i == "A":
            if tiene_cartas_altas(baraja[count+1:count+2]) == False:
                if barajas_restantes >=1:
                    temp +=1
        if i == "J":
            if tiene_cartas_altas(baraja[count+1:count+3]) == False:
                if barajas_restantes >=2:
                    temp +=2
        if i == "Q":
            if tiene_cartas_altas(baraja[count+1:count+4]) == False:
                if barajas_restantes >=3:
                    temp +=3
        if i == "K":
            if tiene_cartas_altas(baraja[count+1:count+5]) == False:
                if barajas_restantes >=4:
                    temp +=4
        if count % 2 == 0:
            jugador_uno += temp
        else:
            jugador_dos += temp
        count += 1    
        temp = 0
        
    return jugador_uno, jugador_dos
    
print(juego(baraja))