# Grupo 11 - Introducción a Señales Biomédicas
Bienvenidos al repositorio del grupo 11 del curso "Introducción a Señales Biomédicas" del ciclo 2023-1

## Nombre del proyecto: Detector semiautomático de arritmias de bajo costo utilizando la señal de ECG

Se realizará un dispositivo que sea capaz de analizar y realizar la detección semiautomática de arritmias a través de la señal de ECG. Se obtendrá, preprocesará y extraerá la información haciendo uso de los conocimientos proporcionados por el curso.

El objetivo de este proyecto es poder proveer un sistema de bajo costo que pueda ser usado en los centros de salud de zonas rurales para realizar procedimientos predictivos de arritmias cardíacas a la población. Para esto se contará con un algoritmo de Machine Learning basado en el uso de autoencoders.

### Tabla de contenidos
- [Integrantes](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#integrantes)
- [Materiales](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#materiales)
- [Documentacion](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#documentaci%C3%B3n)

### Integrantes:

El equipo de trabajo está conformado por los siguientes estudiantes de Ingeniería Biomédica de la Pontificia Universidad Católica del Perú y la Universidad Peruana Cayetano Heredia:

<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/d30d4cc5-f191-4ad5-9e7b-6637fc89b91f)" width="70%">

* Erika Paola Uchuya Trocones (colaborador) - erika.uchuya@upch.pe
* Hector Dair Alegria Cortez (colaborador) - hector.alegria@upch.pe
* Jorge Eduardo Medina Celiz (colaborador) - jorge.medina@upch.pe
* Fernando Eduardo Puipulivia Zarate (colaborador) - fernando.puipulivia@upch.pe
* Felix Renato Rojas Arellanos (colaborador) - felix.rojas@upch.pe

### Materiales:

Lista de materiales necesarios para la adquisición de las señales y el procesamiento inicial de tales datos.

1)  Arduino UNO
  
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/c65b1e9a-f7d6-46b7-9a4a-6c98823b7c68" width="30%">
  
2)  Sensor AD8232  
  
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/02731d09-bf9f-486f-a7d2-d514992b236f" alt="Arduino Nano" width="30%">

3)  Electrodos
  
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/6ca780f5-916c-4248-8b5e-b72ca67d2feb" alt="Arduino Nano" width="30%">

4)  Protoboard
  
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/b9cf64d1-504d-4287-9d97-1629d49fd95f" alt="Arduino Nano" width="30%">

5)  Laptop
  
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/2d945753-a40b-4efe-9e52-deb6eea81b6f" alt="Arduino Nano" width="30%">

  
### Documentación

Se resume en esta sección la documentación tanto a nivel de software como a nivel de hardware del proyecto.
#### Hardware


[Plano de la carcasa del Predictor ECG 250](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Hardware/Plano%20centro%20de%20control%20Predictor%20ECG250.ai)

[Circuito esquemático del proyecto](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Hardware/Circuito%20esquem%C3%A1tico%20Predictor%20ECG250.JPG)

#### Software

[Código para realizar la GUI](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Software/GUI_2.0.py)

[Código de entrenamiento al Predictor ECG 250](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Software/Training_model.ipynb)

[Código que realiza la predicción de arritmias - Predictor ECG 250](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Software/autoencoder.h5)
