# Exemple de graphe animé avec une simple boucle

import numpy as np
from matplotlib import pyplot as plt

sa_liste = np.linspace(0,25,1001)
ma_liste = []
print(sa_liste)
print(len(sa_liste))

for i in range(8):
    
    plt.clf()
    ma_liste = []
    
    for j in sa_liste:
        ma_liste.append(np.sin(j*(i+1)))
        print(len(ma_liste))

    plt.xlim(0,10)
    plt.ylim(-1.25,1.25)
    plt.grid(visible=True)
    plt.plot(sa_liste, ma_liste)
    plt.pause(0.5)


plt.show()
    
    
