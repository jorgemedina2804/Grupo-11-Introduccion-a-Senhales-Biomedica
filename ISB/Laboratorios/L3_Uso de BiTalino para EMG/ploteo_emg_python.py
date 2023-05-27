import numpy as np
import matplotlib.pyplot as plt

# Carga los datos desde un archivo de texto
data = np.loadtxt('RecordEMGintro.txt')

# Usa solo la sexta columna de datos
emg = data[:,5]

# Calcula el tiempo transcurrido entre cada muestra (asumiendo una frecuencia de muestreo de 1000 Hz)
tiempo = np.arange(len(emg)) / 1000

# Crea un gráfico de línea para el canal seleccionado
plt.plot(tiempo, emg)

# Agrega etiquetas de eje y título
plt.xlabel('Tiempo (s)')
plt.ylabel('EMG (mV)')
plt.title('Canal A1 - EMG')

# Muestra el gráfico
plt.savefig('emg_plot.png')
