import numpy as np
import matplotlib.pyplot as plt

# Carga los datos desde un archivo de texto
data1 = np.loadtxt('30 lpm pro sim.txt')
data2 = np.loadtxt('120 lpm pro sim.txt')
data3 = np.loadtxt('240 lpm pro sim.txt')
data4 = np.loadtxt('Arritmia Taq vent 200 lpm prosim.txt')

# Usa solo la sexta columna de datos
ecg1 = data1[:,5]
ecg2 = data2[:,5]
ecg3 = data3[:,5]
ecg4 = data4[:,5]

# Calcula el tiempo transcurrido entre cada muestra (asumiendo una frecuencia de muestreo de 1000 Hz)
tiempo1 = np.arange(len(ecg1)) / 1000
tiempo2 = np.arange(len(ecg2)) / 1000
tiempo3 = np.arange(len(ecg3)) / 1000
tiempo4 = np.arange(len(ecg4)) / 1000

# Dividir el tiempo y los datos ECG en partes iguales
ecg1_seccion = ecg1[:3000]
tiempo1_seccion = tiempo1[:3000]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo1_seccion, ecg1_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG 30 lpm (Pro Sim)')

# Guarda la figura actual en un archivo
plt.savefig('ecg1_plot_30.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Dividir el tiempo y los datos ECG en partes iguales
ecg2_seccion = ecg2[:3000]
tiempo2_seccion = tiempo2[:3000]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo2_seccion, ecg2_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG 120 lpm (Pro Sim)')

# Guarda la figura actual en un archivo
plt.savefig('ecg2_plot_120.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Dividir el tiempo y los datos ECG en partes iguales
ecg3_seccion = ecg3[:3000]
tiempo3_seccion = tiempo3[:3000]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo3_seccion, ecg3_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG 240 lpm (Pro Sim)')

# Guarda la figura actual en un archivo
plt.savefig('ecg3_plot_240.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Dividir el tiempo y los datos ECG en partes iguales
ecg4_seccion = ecg4[:3000]
tiempo4_seccion = tiempo4[:3000]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo4_seccion, ecg4_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG Taquicardia Ventricular 200 lpm (Pro Sim)')

# Guarda la figura actual en un archivo
plt.savefig('ecg4_plot_TV.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()