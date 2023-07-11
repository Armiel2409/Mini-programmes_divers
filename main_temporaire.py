#IMPORTATIONS GÉNÉRALES

import numpy as np

#IMPORTATIONS POUR TRACTER
from matplotlib import pyplot as plt

#IMPORTATIONS PERSONNELLES ET/OU RELATIVES AU PICOSCOPE
from PicoScope import PicoScopeController
from PS5000A import PS5A

from traitement_signal import FILTRAGE_SIGNAL


# DÉCLARATION DE VARIABLES

Frequence = 2
Periodes = 6
ps = PS5A()

# INITIALISATION DU PICOSCOPE

print("• Démarrage du picoscope")

PicoScopeController(verbose=True).get_instruments_by_name(PS5A.NAME) #Détecte le picoscope
print(PicoScopeController(verbose=True).get_instruments_by_name(PS5A.NAME))
ps.open(PS5A.Resolutions.DR15) #Active le picoscope avec une résolution de 15 bits

print("• • • • • Sélection du channel • • • • •")

ps.setup_channel(PS5A.Channels.CHANNEL_A, True, PS5A.Couplings.DC, PS5A.Ranges.R2V , 0)
ps.setup_trigger(True, PS5A.Channels.CHANNEL_A, -25e-3, PS5A.Directions.RISING, 0, 10)
ps.setup_channel(PS5A.Channels.CHANNEL_B, True, PS5A.Couplings.DC, PS5A.Ranges.R1V , 0)
ps.setup_trigger(True, PS5A.Channels.CHANNEL_B, -25e-3, PS5A.Directions.RISING, 0, 10)
ps.setup_timebase(0, int(Periodes*10e2), (Periodes/Frequence))


print("• • • • • Acquisition • • • • •")
# ACQUISITION

ps.output = True

ps.run_capture()
while not ps.is_finished:
    pass #print(ps.status)
ps.output = True
ps.get_data()
    
signal_B = ps.get_channel(PS5A.Channels.CHANNEL_A)
signal_H = ps.get_channel(PS5A.Channels.CHANNEL_B)
temp_H =[]
temps = ps.time

# FILTRAGE

te = 1/(Frequence*10e2)

# TRAITEMENT DU SIGNAL

offset_corrector = 0
B = [(-1)*offset_corrector]
H = [0]
cumul = 0
surface_bobine = 7*10e-3*4.5*10e-3

for i in range(len(signal_B)):
    signal_B[i]=(-1)*signal_B[i] #inverse le signal
    
# FILTRAGE

#freq_B, spectre_B, purified_B = FILTRAGE_SIGNAL(temps, signal_B, dt, 0.00004)

# INTEGRATION (METHODE DES TRAPEZES)

for j in range(len(signal_B)-1):
    cumul+=(temps[j+1]-temps[j])*((signal_B[j+1]+signal_B[j])*0.5)
    B.append(cumul)

cumul = 0

for k in range(len(signal_H)-1):
    cumul+=(temps[k+1]-temps[k])*((signal_H[k+1]+signal_H[k])*0.5)
    H.append(cumul)
    
# CORRECTION DE L'ERREUR

for i in range(len(B)):
    # B[i] = B[i]-(0.02888*temps[i])
    # H[i] = H[i]+(0.01525*temps[i])
    
    B[i] = B[i] - ((B[-1]-B[0])/(temps[-1]-temps[0]))*temps[i]
    H[i] = H[i] - ((H[-1]-H[0])/(temps[-1]-temps[0]))*temps[i]
    

# MOYENNAGE DES VALEURS POUR MISE EN FORME D'HYSTÉRÉSIS

chunk = []
cumulated_chunk = []
compteur = 0


# Séparation en chunks

for i in range(len(B)):
    
    if (temps[i]<compteur):
        chunk.append(B[i])
    
    else :
        print("WOOOU")
        print(temps[i])
        compteur+=(1/Frequence)
        print(len(chunk))
        cumulated_chunk.append(chunk)
        chunk=[B[i]]

for i in range(len(cumulated_chunk)):
    for j in range(len(cumulated_chunk[i])):
        moyenne=cumulated_chunk[i][j]+cumulated_chunk[i+1]
    
# Moyennage 

compteur = 0
moyenne = []

for i in range(len(cumulated_chunk[0])):
    for j in range(len(cumulated_chunk)):
        compteur+=cumulated_chunk[j][i]
    moyenne.append(compteur/len(cumulated_chunk))
    
# TRACÉS DES COURBES

    # Generate subplots
    
fig = plt.figure(figsize=[15,7])
trace_signaux = plt.subplot2grid((2,2),(0,0))
trace_signaux.grid()

trace_integrales = plt.subplot2grid((2,2),(1,0))
trace_integrales.grid()

trace_hysteresis = plt.subplot2grid((1,2),(0,1))
trace_hysteresis.grid()

    # Trace
    
trace_signaux.plot(temps, signal_B)
trace_signaux.plot(temps, signal_H)

trace_integrales.plot(temps, B)
trace_integrales.plot(temps, H)

#trace_hysteresis.plot(signal_H, signal_B)
trace_hysteresis.plot(H,B)



ps.close()



