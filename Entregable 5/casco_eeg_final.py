import numpy as np
import matplotlib.pyplot as plt
import os

ruta = "C:/Users/dairc/Desktop/Dair/UNIVERSIDAD/2023-1/Introducción a Señales Biomédicas/EEG"
os.chdir(ruta)

canal1=[]
canal2=[]
canal3=[]
canal4=[]
canal5=[]
canal6=[]
canal7=[]
canal8=[]

with open("OpenBCI-RAW-2023-04-21_12-33-00.txt", "r") as archivo:
    # Saltar la primera línea que contiene los encabezados
    archivo.readline()
    # Iterar sobre cada línea del archivo
    for linea in archivo:
        # Dividir la línea en columnas utilizando la coma como separador
        columnas = linea.strip().split(", ")
        canal1.append(float(columnas[1]))
        canal2.append(float(columnas[2]))
        canal3.append(float(columnas[3]))
        canal4.append(float(columnas[4]))
        canal5.append(float(columnas[5]))
        canal6.append(float(columnas[6]))
        canal7.append(float(columnas[7]))
        canal8.append(float(columnas[8]))

# De uV a mV (Etapa de Conversión)
canal1 = np.multiply(canal1, 1000)
canal2 = np.multiply(canal2, 1000)
canal3 = np.multiply(canal3, 1000)
canal4 = np.multiply(canal4, 1000)
canal5 = np.multiply(canal5, 1000)
canal6 = np.multiply(canal6, 1000)
canal7 = np.multiply(canal7, 1000)
canal8 = np.multiply(canal8, 1000)

# TODOS LOS CANALES
###########################################################

time1 = np.arange(len(canal1[:5750])) / 160
time2 = np.arange(len(canal1[5760:17900])) / 160
time3 = np.arange(len(canal1[17920:len(canal1)])) / 160

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(time1, canal1[:5750], label='Canal 1')
plt.plot(time1, canal2[:5750], label='Canal 2')
plt.plot(time1, canal3[:5750], label='Canal 3')
plt.plot(time1, canal4[:5750], label='Canal 4')
plt.plot(time1, canal5[:5750], label='Canal 5')
plt.plot(time1, canal6[:5750], label='Canal 6')
plt.plot(time1, canal7[:5750], label='Canal 7')
plt.plot(time1, canal8[:5750], label='Canal 8')

plt.title('MULTICHANNEL - LINEA BASE')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend()

# Guarda la figura actual en un archivo
plt.savefig('eeg_multichannel_CASCO_1.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(time2, canal1[5760:17900], label='Canal 1')
plt.plot(time2, canal2[5760:17900], label='Canal 2')
plt.plot(time2, canal3[5760:17900], label='Canal 3')
plt.plot(time2, canal4[5760:17900], label='Canal 4')
plt.plot(time2, canal5[5760:17900], label='Canal 5')
plt.plot(time2, canal6[5760:17900], label='Canal 6')
plt.plot(time2, canal7[5760:17900], label='Canal 7')
plt.plot(time2, canal8[5760:17900], label='Canal 8')
plt.title('MULTICHANNEL - ABRIR Y CERRAR EN INTEERVALOS')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend()

# Guarda la figura actual en un archivo
plt.savefig('eeg_multichannel_CASCO_2.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(time3, canal1[17920:len(canal1)], label='Canal 1')
plt.plot(time3, canal2[17920:len(canal1)], label='Canal 2')
plt.plot(time3, canal3[17920:len(canal1)], label='Canal 3')
plt.plot(time3, canal4[17920:len(canal1)], label='Canal 4')
plt.plot(time3, canal5[17920:len(canal1)], label='Canal 5')
plt.plot(time3, canal6[17920:len(canal1)], label='Canal 6')
plt.plot(time3, canal7[17920:len(canal1)], label='Canal 7')
plt.plot(time3, canal8[17920:len(canal1)], label='Canal 8')
plt.title('MULTICHANNEL - EJERCICIOS MATEMATICOS')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.legend()

# Guarda la figura actual en un archivo
plt.savefig('eeg_multichannel_CASCO_3.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()