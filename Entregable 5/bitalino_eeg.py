import numpy as np
import matplotlib.pyplot as plt
import os

ruta = "C:/Users/dairc/Desktop/Dair/UNIVERSIDAD/2023-1/Introducción a Señales Biomédicas/EEG"
os.chdir(ruta)

# Carga los datos desde un archivo de texto
data1 = np.loadtxt('1. EEG 30 segundos ojos cerrados.txt')
data2 = np.loadtxt('2. Intervalos 5 segundos.txt')
data3 = np.loadtxt('3. Repeticion paso 1.txt')
data4 = np.loadtxt('4. Ejercicio matematico.txt')
data5 = np.loadtxt('5. Flash.txt')

# Usa solo la sexta columna de datos
eeg1 = data1[:,5]
eeg2 = data2[:,5]
eeg3 = data3[:,5]
eeg4 = data4[:,5]
eeg5 = data5[:,5]

# Calcula el tiempo transcurrido entre cada muestra (asumiendo una frecuencia de muestreo de 1000 Hz)
tiempo1 = np.arange(len(eeg1)) / 1000
tiempo2 = np.arange(len(eeg2)) / 1000
tiempo3 = np.arange(len(eeg3)) / 1000
tiempo4 = np.arange(len(eeg4)) / 1000
tiempo5 = np.arange(len(eeg5)) / 1000

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo1, eeg1)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG 30 segundos ojos cerrados')

# Guarda la figura actual en un archivo
plt.savefig('eeg1_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo2, eeg2)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG intervalo 5 segundos')

# Guarda la figura actual en un archivo
plt.savefig('eeg2_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo3, eeg3)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG Repetición paso 1')

# Guarda la figura actual en un archivo
plt.savefig('eeg3_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo4, eeg4)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG Ejercicio matemático')

# Guarda la figura actual en un archivo
plt.savefig('eeg4_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo5, eeg5)
plt.xlabel('Tiempo (s)')
plt.ylabel('EEG (mV)')
plt.title('EEG Flash')

# Guarda la figura actual en un archivo
plt.savefig('eeg5_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()
