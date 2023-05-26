import numpy as np
import matplotlib.pyplot as plt

# Carga los datos desde un archivo de texto
data2 = np.loadtxt('ecg 10 segundos.txt')
data3 = np.loadtxt('ECG con ejercicio.txt')
data1 = np.loadtxt('ECG tranquilo.txt')

# Usa solo la sexta columna de datos
ecg1 = data1[:,5]
ecg2 = data2[:,5]
ecg3 = data3[:,5]

# Calcula el tiempo transcurrido entre cada muestra (asumiendo una frecuencia de muestreo de 1000 Hz)
tiempo1 = np.arange(len(ecg1)) / 1000
tiempo2 = np.arange(len(ecg2)) / 1000
tiempo3 = np.arange(len(ecg3)) / 1000

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo1, ecg1)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG Estado Basal')

# Guarda la figura actual en un archivo
plt.savefig('ecg1_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo2, ecg2)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG 10 segundos')

# Guarda la figura actual en un archivo
plt.savefig('ecg2_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo3, ecg3)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG Actividad Física')

# Guarda la figura actual en un archivo
plt.savefig('ecg3_plot.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()