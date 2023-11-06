import csv
import pandas as pd
import json

def clima():

    df = pd.read_csv('misiontic\data.csv')

   # Filtering the dataframe by location 1.
    l1=df[(df['location']==1)]
    l2=df[(df['location']==2)]
    l3=df[(df['location']==3)]
    l4=df[(df['location']==4)]
    l5=df[(df['location']==5)]

    pt1 = l1['temperature'].mean()
    pp1 = l1['pressure'].mean()

    # Getting the mean of the temperature column for location 2.
    pt2 = l2['temperature'].mean()
    pp2 = l2['pressure'].mean()

    pt3 = l3['temperature'].mean()
    pp3 = l3['pressure'].mean()

    pt4 = l4['temperature'].mean()
    pp4 = l4['pressure'].mean()

    pt5 = l5['temperature'].mean()
    pp5 = l5['pressure'].mean()

    dicprom = {"1": [pt1,pp1],
            "2": [pt2,pp2],
            "3": [pt3,pp3],
            "4": [pt4,pp4],
            "5": [pt5,pp5]}

    with open("promedioos.json", "w") as prome:
        
        json.dump(dicprom,prome)
        return prome

print(clima())