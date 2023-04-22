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

canal1_1 = canal1[:5750]
canal1_2 = canal1[5760:17900]
canal1_3 = canal1[17920:len(canal1)]

canal2_1 = canal2[:5750]
canal2_2 = canal2[5760:17900]
canal2_3 = canal2[17920:len(canal1)]

canal3_1 = canal3[:5750]
canal3_2 = canal3[5760:17900]
canal3_3 = canal3[17920:len(canal1)]

canal4_1 = canal4[:5750]
canal4_2 = canal4[5760:17900]
canal4_3 = canal4[17920:len(canal1)]

canal5_1 = canal5[:5750]
canal5_2 = canal5[5760:17900]
canal5_3 = canal5[17920:len(canal1)]

canal6_1 = canal6[:5750]
canal6_2 = canal6[5760:17900]
canal6_3 = canal6[17920:len(canal1)]

canal7_1 = canal7[:5750]
canal7_2 = canal7[5760:17900]
canal7_3 = canal7[17920:len(canal1)]

canal8_1 = canal8[:5750]
canal8_2 = canal8[5760:17900]
canal8_3 = canal8[17920:len(canal1)]

# TRAMO 1

psd1, freq1 = plt.psd(canal1_1, 512, 160)
psd1 = np.where(psd1 > 0, psd1, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq1, 10 * np.log10(psd1), label="Ch1")

psd2, freq2 = plt.psd(canal2_1, 512, 160)
psd2 = np.where(psd2 > 0, psd2, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq2, 10 * np.log10(psd2), label="Ch2")

psd3, freq3 = plt.psd(canal3_1, 512, 160)
psd3 = np.where(psd3 > 0, psd3, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq3, 10 * np.log10(psd3), label="Ch3")

psd4, freq4 = plt.psd(canal4_1, 512, 160)
psd4 = np.where(psd4 > 0, psd4, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq4, 10 * np.log10(psd4), label="Ch4")

psd5, freq5 = plt.psd(canal5_1, 512, 160)
psd5 = np.where(psd5 > 0, psd5, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq5, 10 * np.log10(psd5), label="Ch5")

psd6, freq6 = plt.psd(canal6_1, 512, 160)
psd6 = np.where(psd6 > 0, psd6, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq6, 10 * np.log10(psd6), label="Ch6")

psd7, freq7 = plt.psd(canal7_1, 512, 160)
psd7 = np.where(psd7 > 0, psd7, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq7, 10 * np.log10(psd7), label="Ch7")

psd8, freq8 = plt.psd(canal8_1, 512, 160)
psd8 = np.where(psd8 > 0, psd8, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq8, 10 * np.log10(psd8), label="Ch8")

plt.legend(loc="upper right")
plt.title("PSD para FFT del TRAMO 1")

# Guarda la figura actual en un archivo
plt.savefig('eeg_multichannel_CASCO_psd1.png')
plt.show()

# TRAMO 2

psd1, freq1 = plt.psd(canal1_2, 512, 160)
psd1 = np.where(psd1 > 0, psd1, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq1, 10 * np.log10(psd1), label="Ch1")

psd2, freq2 = plt.psd(canal2_2, 512, 160)
psd2 = np.where(psd2 > 0, psd2, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq2, 10 * np.log10(psd2), label="Ch2")

psd3, freq3 = plt.psd(canal3_2, 512, 160)
psd3 = np.where(psd3 > 0, psd3, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq3, 10 * np.log10(psd3), label="Ch3")

psd4, freq4 = plt.psd(canal4_2, 512, 160)
psd4 = np.where(psd4 > 0, psd4, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq4, 10 * np.log10(psd4), label="Ch4")

psd5, freq5 = plt.psd(canal5_2, 512, 160)
psd5 = np.where(psd5 > 0, psd5, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq5, 10 * np.log10(psd5), label="Ch5")

psd6, freq6 = plt.psd(canal6_2, 512, 160)
psd6 = np.where(psd6 > 0, psd6, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq6, 10 * np.log10(psd6), label="Ch6")

psd7, freq7 = plt.psd(canal7_2, 512, 160)
psd7 = np.where(psd7 > 0, psd7, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq7, 10 * np.log10(psd7), label="Ch7")

psd8, freq8 = plt.psd(canal8_2, 512, 160)
psd8 = np.where(psd8 > 0, psd8, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq8, 10 * np.log10(psd8), label="Ch8")

plt.legend(loc="upper right")
plt.title("PSD para FFT del TRAMO 2")

# Guarda la figura actual en un archivo
plt.savefig('eeg_multichannel_CASCO_psd2.png')
plt.show()

# TRAMO 3

psd1, freq1 = plt.psd(canal1_3, 512, 160)
psd1 = np.where(psd1 > 0, psd1, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq1, 10 * np.log10(psd1), label="Ch1")

psd2, freq2 = plt.psd(canal2_3, 512, 160)
psd2 = np.where(psd2 > 0, psd2, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq2, 10 * np.log10(psd2), label="Ch2")

psd3, freq3 = plt.psd(canal3_3, 512, 160)
psd3 = np.where(psd3 > 0, psd3, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq3, 10 * np.log10(psd3), label="Ch3")

psd4, freq4 = plt.psd(canal4_3, 512, 160)
psd4 = np.where(psd4 > 0, psd4, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq4, 10 * np.log10(psd4), label="Ch4")

psd5, freq5 = plt.psd(canal5_3, 512, 160)
psd5 = np.where(psd5 > 0, psd5, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq5, 10 * np.log10(psd5), label="Ch5")

psd6, freq6 = plt.psd(canal6_3, 512, 160)
psd6 = np.where(psd6 > 0, psd6, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq6, 10 * np.log10(psd6), label="Ch6")

psd7, freq7 = plt.psd(canal7_3, 512, 160)
psd7 = np.where(psd7 > 0, psd7, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq7, 10 * np.log10(psd7), label="Ch7")

psd8, freq8 = plt.psd(canal8_3, 512, 160)
psd8 = np.where(psd8 > 0, psd8, 1e-16)  # Agregar un valor pequeño a los valores iguales a cero
plt.plot(freq8, 10 * np.log10(psd8), label="Ch8")

plt.legend(loc="upper right")
plt.title("PSD para FFT del TRAMO 3")

# Guarda la figura actual en un archivo
plt.savefig('eeg_multichannel_CASCO_psd3.png')
plt.show()