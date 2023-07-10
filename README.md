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
1. Predictor ECG 250 ensamblado
 <p align="center">
<img width="400" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/071bf1d5-0b1d-48eb-81bd-a4262a52d9b0" >

2. Indicadores visuales del Predictor ECG 250:
   
   LED Verde: indica que el dispositivo está listo para ser usado
   
   LED Azul: Mientras está encendido significa que se encuentra recolectando los datos del usuario
   
<p align="center">
<img width="400" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/453a0cf8-eea6-47be-bda7-8a4c79a4ca9a)" >

3. Prueba del Predictor ECG 250 en el primer sujeto de prueba
<p align="center">
<img width="400" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/ac90a259-4485-4f59-a478-f1437d828cff" >
   
4. Prueba del Predictor ECG 250 en el segundo sujeto de prueba
<img width="400" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/1846af42-5744-4b20-b89a-cfc6fe80443d" >
   

[Plano de la carcasa del Predictor ECG 250](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Hardware/Plano%20centro%20de%20control%20Predictor%20ECG250.ai)

[Circuito esquemático del proyecto](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Hardware/Circuito%20esquem%C3%A1tico%20Predictor%20ECG250.JPG)

#### Software

1. Adquisición de la señal ECG haciendo uso del módulo AD8232 conectado al Arduino UNO
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/88c9df7d-e2f6-428b-af64-41071b340034" >

2. Aplicación del filtro pasabajo

<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/313f80f6-b9a3-42e1-8998-3daf72d05d39" >

3. Señal ECG post filtro pasabajo
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/7f80027e-3def-4a8c-9e9d-2f536ab8fc97" >
   
4. Picos de la señal ECG
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/8b636648-dfc5-4e76-94c3-b2e9c20b2ffd" >
   
5. Verificación de los latidos post downsampling

<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/b9b17156-6fb2-4633-9e74-2a2cca10a284" >

6. Mean Absolute Error
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/44a432c2-24ee-4a50-af96-96b297e15366" >  

7. Interfaz gráfica interactiva 
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/assets/111662394/168d8869-090a-4f4d-9e58-2ad3501c7747" >  

[Código para realizar la GUI](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Software/GUI_2.0.py)

[Código Predictor ECG 250](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Software/Training_model.ipynb)

[Código que exporta el modelo entrenado - Predictor ECG 250](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Software/autoencoder.h5)

#### Paper del proyecto 
