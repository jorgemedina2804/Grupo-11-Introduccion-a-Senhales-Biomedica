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
print(len(tiempo1))
print(len(tiempo2))
print(len(tiempo3))

# Dividir el tiempo y los datos ECG en partes iguales
ecg1_seccion = ecg1[:2500]
tiempo1_seccion = tiempo1[:2500]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo1_seccion, ecg1_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG Estado Basal (sección seleccionada)')

# Guarda la figura actual en un archivo
plt.savefig('ecg1_plot_sec.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Dividir el tiempo y los datos ECG en partes iguales
ecg2_seccion = ecg2[:2500]
tiempo2_seccion = tiempo2[:2500]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo2_seccion, ecg2_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG 10 segundos (sección seleccionada)')

# Guarda la figura actual en un archivo
plt.savefig('ecg2_plot_sec.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()

# Crea una nueva figura
plt.figure()

# Dividir el tiempo y los datos ECG en partes iguales
ecg3_seccion = ecg3[:2500]
tiempo3_seccion = tiempo3[:2500]

# Crear un gráfico de línea para la sección seleccionada
plt.plot(tiempo3_seccion, ecg3_seccion)
plt.xlabel('Tiempo (s)')
plt.ylabel('ECG (mV)')
plt.title('Canal A2 - ECG Actividad Física (sección seleccionada)')

# Guarda la figura actual en un archivo
plt.savefig('ecg3_plot_sec.png')

# Muestra el gráfico
plt.show()

# Cierra la figura actual
plt.close()