from matplotlib import pyplot as plt
import numpy as np

sa_liste = np.linspace(0,25,101)
ma_liste = []
autre_liste = []

for i in range(len(sa_liste)):
    ma_liste.append(np.sin(sa_liste[i]))
    autre_liste.append(np.cos(sa_liste[i]))
    
fig = plt.figure(figsize=[16,5])

mon_trace = plt.subplot2grid((1,2),(0,0))
autre_trace = plt.subplot2grid((1,2),(0,1))

mon_trace.plot(sa_liste, ma_liste)
autre_trace.plot(autre_liste, ma_liste)

plt.show()