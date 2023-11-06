from fileinput import close
import json
import csv

def clima():
    
    with open('misiontic\data.csv', newline='') as csvfile:
        pt1 = 0
        pp1 = 0
        pt2 = 0
        pp2 = 0
        pt3 = 0
        pp3 = 0
        pt4 = 0
        pp4 = 0
        pt5 = 0
        pp5 = 0
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        reader = csv.DictReader(csvfile)
        lista = []
        for row in reader:
            lista.append(row)
        for lis in lista:
            if lis['location'] == '1':
                pt1 += int(lis['temperature'])
                pp1 += int(lis['pressure'])
                c1 +=1
            if lis['location'] == '2':
                pt2 += int(lis['temperature'])
                pp2 += int(lis['pressure'])
                c2 +=1
            if lis['location'] == '3':
                pt3 += int(lis['temperature'])
                pp3 += int(lis['pressure'])
                c3 +=1
            if lis['location'] == '4':
                pt4 += int(lis['temperature'])
                pp4 += int(lis['pressure'])
                c4 +=1
            if lis['location'] == '5':
                pt5 += int(lis['temperature'])
                pp5 += int(lis['pressure'])
                c5 +=1
        pt1 = round(pt1/c1,1)
        pp1 = round(pp1/c1,1)
        pt2 = round(pt2/c2,1)
        pp2 = round(pp2/c2,1)
        pt3 = round(pt3/c3,1)
        pp3 = round(pp3/c3,1)
        pt4 = round(pt4/c4,1)
        pp4 = round(pp4/c4,1)
        pt5 = round(pt5/c5,1)
        pp5 = round(pp5/c5,1)
        diccionario_promedios = {"1": [pt1,pp1],
            "2": [pt2,pp2],
            "3": [pt3,pp3],
            "4": [pt4,pp4],
            "5": [pt5,pp5]}
        csvfile.close()
        
    with open('promedio.json', 'w') as datos:
        datos = json.dumps(diccionario_promedios)
        
    
    

    with open ('data_nuevo.csv', 'w') as file:
        id = 1
        writer = csv.writer(file)
        writer.writerow(['id','location','temperature','pressure', 'above_avg_temp', 'above_avg_pres'])
        for lis in lista:
            if lis['location'] == '1':
                if int(lis['temperature']) > pt1 and int(lis['pressure']) > pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "SI"])
                elif int(lis['temperature']) > pt1 and int(lis['pressure']) < pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "NO"])
                elif int(lis['temperature']) < pt1 and int(lis['pressure']) > pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "SI"])
                elif int(lis['temperature']) < pt1 and int(lis['pressure']) < pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "NO"])
                elif int(lis['temperature']) == pt1 and int(lis['pressure']) == pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "IGUAL"])
                elif int(lis['temperature']) == pt1 and int(lis['pressure']) < pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "NO"])
                elif int(lis['temperature']) < pt1 and int(lis['pressure']) == pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "IGUAL"])
                elif int(lis['temperature']) > pt1 and int(lis['pressure']) == pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "IGUAL"])
                elif int(lis['temperature']) == pt1 and int(lis['pressure']) > pp1:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "SI"])
                id += 1
            if lis['location'] == '2':
                if int(lis['temperature']) > pt2 and int(lis['pressure']) > pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "SI"])
                elif int(lis['temperature']) > pt2 and int(lis['pressure']) < pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "NO"])
                elif int(lis['temperature']) < pt2 and int(lis['pressure']) > pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "SI"])
                elif int(lis['temperature']) < pt2 and int(lis['pressure']) < pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "NO"])
                elif int(lis['temperature']) == pt2 and int(lis['pressure']) == pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "IGUAL"])
                elif int(lis['temperature']) == pt2 and int(lis['pressure']) < pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "NO"])
                elif int(lis['temperature']) < pt2 and int(lis['pressure']) == pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "IGUAL"])
                elif int(lis['temperature']) > pt2 and int(lis['pressure']) == pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "IGUAL"])
                elif int(lis['temperature']) == pt2 and int(lis['pressure']) > pp2:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "SI"])
                id += 1
            if lis['location'] == '3':
                if int(lis['temperature']) > pt3 and int(lis['pressure']) > pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "SI"])
                elif int(lis['temperature']) > pt3 and int(lis['pressure']) < pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "NO"])
                elif int(lis['temperature']) < pt3 and int(lis['pressure']) > pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "SI"])
                elif int(lis['temperature']) < pt3 and int(lis['pressure']) < pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "NO"])
                elif int(lis['temperature']) == pt3 and int(lis['pressure']) == pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "IGUAL"])
                elif int(lis['temperature']) == pt3 and int(lis['pressure']) < pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "NO"])
                elif int(lis['temperature']) < pt3 and int(lis['pressure']) == pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "IGUAL"])
                elif int(lis['temperature']) > pt3 and int(lis['pressure']) == pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "IGUAL"])
                elif int(lis['temperature']) == pt3 and int(lis['pressure']) > pp3:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "SI"])
                id = id + 1
            if lis['location'] == '4':
                if int(lis['temperature']) > pt4 and int(lis['pressure']) > pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "SI"])
                elif int(lis['temperature']) > pt4 and int(lis['pressure']) < pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "NO"])
                elif int(lis['temperature']) < pt4 and int(lis['pressure']) > pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "SI"])
                elif int(lis['temperature']) < pt4 and int(lis['pressure']) < pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "NO"])
                elif int(lis['temperature']) == pt4 and int(lis['pressure']) == pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "IGUAL"])
                elif int(lis['temperature']) == pt4 and int(lis['pressure']) < pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "NO"])
                elif int(lis['temperature']) < pt4 and int(lis['pressure']) == pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "IGUAL"])
                elif int(lis['temperature']) > pt4 and int(lis['pressure']) == pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "IGUAL"])
                elif int(lis['temperature']) == pt4 and int(lis['pressure']) > pp4:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "SI"])
                id = id + 1    
            if lis['location'] == '5':
                if int(lis['temperature']) > pt5 and int(lis['pressure']) > pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "SI"])
                elif int(lis['temperature']) > pt5 and int(lis['pressure']) < pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "NO"])
                elif int(lis['temperature']) < pt5 and int(lis['pressure']) > pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "SI"])
                elif int(lis['temperature']) < pt5 and int(lis['pressure']) < pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "NO"])
                elif int(lis['temperature']) == pt5 and int(lis['pressure']) == pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "IGUAL"])
                elif int(lis['temperature']) == pt5 and int(lis['pressure']) < pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "NO"])
                elif int(lis['temperature']) < pt5 and int(lis['pressure']) == pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "NO", "IGUAL"])
                elif int(lis['temperature']) > pt5 and int(lis['pressure']) == pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "SI", "IGUAL"])
                elif int(lis['temperature']) == pt5 and int(lis['pressure']) > pp5:
                    writer.writerow([id,lis['location'],lis['temperature'],lis['pressure'], "IGUAL", "SI"])
                id = id + 1
    return datos

print (clima())
            
                    
            
