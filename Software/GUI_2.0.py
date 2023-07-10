import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.interpolate import interp1d
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from scipy.signal import iirnotch, iirfilter, lfilter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tensorflow as tf

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Predictor ECG250")

ventana.configure(bg="darkgray")
# Configurar el tamaño de la ventana
ventana.geometry("800x600")  # Ancho x Alto

def adquirir_ecg(puerto_serie='COM8', velocidad=9600):
    # Inicializa la conexión del puerto serie
    arduino = serial.Serial(puerto_serie, velocidad)

    # Variables para almacenar los datos del ECG
    tiempo_total = 5  # Duración en segundos de la adquisición
    frecuencia_muestreo = 250  # Frecuencia de muestreo del Arduino Uno en Hz
    muestras_totales = tiempo_total * frecuencia_muestreo

    buffer_ecg = []

    def recibir_datos():
        try:
            # Leer los datos enviados durante 5 segundos
            data = arduino.readline().decode().strip()
            print(data)
            # Suponiendo que los datos son enviados en un formato separado por comas y son valores flotantes
            valores_ecg = data.split(',')
            valores_ecg.pop()
            print(valores_ecg)
            for item in valores_ecg:
                buffer_ecg.append(float(item))
        finally:
            # Cerrar la conexión del puerto serie al finalizar la lectura
            arduino.close()

    transmision_iniciada = False
    while not transmision_iniciada:
        data = arduino.readline().decode().strip()
        if data == "START":
            transmision_iniciada = True
            #print("Se inició la transmisión de datos y adquiriendo los 5 segundos de señal.")
            estado_label.config(text="Inició la adquisición (Duración: 5 segundos)")
            recibir_datos()

    # Convertir el buffer_ecg en un arreglo numpy para facilitar el procesamiento
    ecg_np = np.array(buffer_ecg, dtype=float)
    #print(ecg_np)
    # Retornar los datos del ECG procesados (si es necesario)
    return ecg_np  # Cambia esto si quieres retornar el resultado del procesamiento


def preprocesar_ecg(ecg_np, frecuencia_muestreo=250):
    # Detectar los picos R en la señal ECG
    picos_r, _ = find_peaks(ecg_np, height=0.5, distance=100)

    # Crear un arreglo de tiempo para la señal
    mtime = np.linspace(0, 5, 1250)
    print(mtime)
    print(len(mtime))

    # Utilizar filtro Notch para quitar frecuencias que hagan ruido
    f0 = 60.0  # Frecuencia que queremos filtrar (Hz)
    Q = 20.0  # Factor de Calidad
    # Diseño de filtro Notch
    b, a = iirnotch(f0, Q, frecuencia_muestreo)
    y = lfilter(b, a, ecg_np)

    # Filtro pasa bajo para eliminar altas frecuencias y ruido
    b, a = iirfilter(2, 35.0, btype='lowpass', rs=3, ftype='butter', fs=frecuencia_muestreo)
    fpb_signal = lfilter(b, a, y)

    # Retornar los resultados del preprocesamiento que desees utilizar en la GUI
    return fpb_signal

def normalizar_y_segmentar_ecg(ecg_np, longitud_latido=140, altura_minima_pico=0.5, distancia_minima_picos=100):
    # Normalizar el ECG utilizando MinMaxScaler
    min_max_scaler = MinMaxScaler()
    ecg_np_reshaped = ecg_np.reshape(-1, 1)
    ecg_np_normalized = min_max_scaler.fit_transform(ecg_np_reshaped)
    ecg_np_normalized = ecg_np_normalized.reshape(ecg_np.shape)

    # Detectar los picos R en la señal ECG normalizada
    picos_r, _ = find_peaks(ecg_np_normalized, height=altura_minima_pico, distance=distancia_minima_picos)

    # Downsampling mediante interpolación para tener "longitud_latido" datos por cada latido
    latidos_interp = []
    for pico in picos_r[:-1]:
        inicio = max(0, pico)
        fin = min(len(ecg_np_normalized), pico + longitud_latido)
        latido = ecg_np_normalized[inicio:fin]

        indices_originales = np.linspace(0, len(latido) - 1, len(latido))
        indices_interp = np.linspace(0, len(latido) - 1, longitud_latido)
        interpolador = interp1d(indices_originales, latido, kind='cubic')
        latido_interp = interpolador(indices_interp)

        latidos_interp.append(latido_interp)

    # Convertir latidos_interp en un arreglo numpy
    latidos_interp = np.array(latidos_interp)

    # Retornar los latidos segmentados y normalizados
    return latidos_interp

def clasificar_latidos(latidos):
    global perdida
    # Cargar el modelo autoencoder (asegúrate de tener el archivo "autoencoder.h5" en la ruta correcta)
    modelo = load_model("autoencoder.h5")
    # Obtén las reconstrucciones de los latidos utilizando el modelo de autoencoder
    reconstrucciones = modelo.predict(latidos)
    # Calcula la pérdida (MAE) entre los latidos originales y sus reconstrucciones
    perdida = tf.keras.losses.mae(reconstrucciones, latidos).numpy()
    #perdida = np.mean(np.abs(reconstrucciones - latidos), axis=1)
    print("La perdida es: ", perdida)
    # Supongamos que el umbral utilizado para clasificar los latidos es 0.13 (puedes ajustarlo según tus necesidades)
    umbral = 0.13
    # Aplica el umbral para clasificar los latidos en normales (clase 1) y anormales (clase 0)
    clases_latidos = (perdida < umbral).astype(int)
    
    return clases_latidos

def mostrar_diagnostico(clases_latidos):
    # Contar la cantidad de 0 y 1 en el array clases_latidos
    cantidad_0 = sum(clases_latidos == 0)
    cantidad_1 = sum(clases_latidos == 1)

    # Obtener la longitud del array clases_latidos
    total_latidos = len(clases_latidos)
    if cantidad_0 > cantidad_1:
        diagnostico = "La señal corresponde a una arritmia."
    elif cantidad_1 > cantidad_0:
        diagnostico = "La señal corresponde a un ritmo normal."
    else:
        diagnostico = "No se pudo obtener una detección adecuada. Se sugiere volver a realizar la medición."

    resultado_label.config(text="Diagnóstico: " + diagnostico)

def mostrar_imagen_matplotlib(fig):
    # Limpia los widgets dentro del cuadro antes de agregar el nuevo widget de Canvas
    for widget in figura_frame.winfo_children():
        widget.destroy()

    # Convierte la figura de matplotlib a un widget de Canvas de tkinter
    canvas = FigureCanvasTkAgg(fig, master=figura_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    ventana.update_idletasks()

def plotear_señal(ecg_np):
    fig = plt.figure(figsize=(6, 2))
    plt.plot(ecg_np*(10**-2))
    plt.title('Señal ECG')
    plt.xlabel('Muestras')
    plt.ylabel('Amplitud (mV)')
    plt.grid(True)
    plt.tight_layout()
    return fig

def plotear_clasificacion(perdida):
    fig = plt.figure(figsize=(6, 2))
    plt.hist(perdida[None,:], bins=100, alpha=0.75, label='Señal Adquirida')
    plt.xlabel('Pérdidas (MAE)')
    plt.ylabel('Nro. ejemplos')
    plt.legend(loc='upper right')
    plt.vlines(0.13,0,4,'k')
    return fig

# Agregar un botón para realizar la clasificación y ver el resultado
def realizar_adquisicion():
    signal = adquirir_ecg()
    actualizar_etiqueta("Señal adquirida con éxito...")

    signal_pre = preprocesar_ecg(signal)
    latidos = normalizar_y_segmentar_ecg(signal_pre)
    # Mostrar la señal ECG procesada en la GUI
    fig = plotear_señal(signal_pre)
    mostrar_imagen_matplotlib(fig)
    return latidos

def realizar_clasificacion():
    global perdida
    global latidos
    if latidos is not None:
        # Actualizar el estado en la GUI
        actualizar_etiqueta("Realizando clasificación...")

        # Clasificar los latidos utilizando el modelo
        clases_latidos = clasificar_latidos(latidos)

        # Mostrar el resultado de la clasificación en la GUI
        mostrar_diagnostico(clases_latidos)

        # Actualizar el estado en la GUI
        actualizar_etiqueta("Clasificación realizada correctamente.")
        fig = plotear_clasificacion(perdida)
        mostrar_imagen_matplotlib(fig)
    else:
        actualizar_etiqueta("Primero debes adquirir los latidos.")

def cerrar_gui():
    # Cierra la ventana principal
    ventana.destroy()

def actualizar_etiqueta(texto):
    estado_label.config(text=texto)
    ventana.update_idletasks()

def iniciar():
    global latidos
    latidos = None
    actualizar_etiqueta("Presione el botón del dispositivo")
    latidos=realizar_adquisicion()

def ver_segmentacion(latidos):
    # Crear una nueva ventana emergente
    segmentacion_window = tk.Toplevel(ventana)
    segmentacion_window.title("Segmentación de Latidos")

    # Crear una figura de matplotlib y graficar los latidos en la nueva ventana
    fig=plt.figure(figsize=(10, 4))
    for latidos in latidos:
        plt.plot(latidos)
    plt.title('Latidos Segmentados')
    canvas = FigureCanvasTkAgg(fig, master=segmentacion_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Agregar una etiqueta para mostrar el estado de la medición
estado_label = tk.Label(ventana, text="Bienvenido a Predictor ECG250", font=("Arial", 18, "bold"), fg="white", bg="darkgray")
estado_label.pack(pady=10)

# Cambiar el color de fondo y de texto de la etiqueta de diagnóstico
resultado_label = tk.Label(ventana, text="", font=("Arial", 18, "bold"), fg="white", bg="darkgray")
resultado_label.pack(pady=10)

# Cambiar el color de fondo y de texto del botón de clasificación
iniciar_btn = tk.Button(ventana, text="Iniciar", font=("Arial", 16, "bold"), command=iniciar, bg="darkblue", fg="white")
iniciar_btn.pack(pady=5)

# Cambiar el color de fondo y de texto del botón de clasificación
clasificar_btn = tk.Button(ventana, text="Predecir", font=("Arial", 16, "bold"), command=realizar_clasificacion, bg="darkgreen", fg="white")
clasificar_btn.pack(pady=5)

# Botón "Ver Segmentación"
ver_segmentacion_btn = tk.Button(ventana, text="Ver Segmentación", command=lambda: ver_segmentacion(latidos))
ver_segmentacion_btn.pack(side="bottom", padx=10, pady=10, anchor="se")

# Cambiar el color de fondo y de texto del botón de cierre
cerrar_btn = tk.Button(ventana, text="Cerrar", font=("Arial", 12), command=cerrar_gui, bg="darkred", fg="white")
cerrar_btn.place(x=700, y=10)

# Cambiar el color de fondo del cuadro de la figura
figura_frame = tk.Frame(ventana, width=600, height=200, bg='black')
figura_frame.pack(pady=10)

# Agregar el nombre del proyecto en la esquina inferior izquierda
nombre_proyecto_label = tk.Label(ventana, text="Predictor ECG250 by Grupo 11", font=("Roboto", 12), fg="black", bg="darkgray")
nombre_proyecto_label.place(x=10, y=550)

# Ejecutar el bucle principal de la GUI
ventana.mainloop()