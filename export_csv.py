import csv
import numpy as np

sa_liste = np.linspace(0,25,101)
ma_liste = []

for i in sa_liste :
    ma_liste.append(np.sin(i))

with open('Fichier.csv', mode='w', newline='') as fichier :
    
    nom_colonnes = ['Colonne_1', 'Colonne_2']   
    writer = csv.DictWriter(fichier, fieldnames=nom_colonnes)
    writer.writeheader()
    
    for j in range(len(ma_liste)) :
        writer.writerow({'Colonne_1':sa_liste[j], 'Colonne_2':ma_liste[j]})
        
