# Entregable 5 - Uso de BiTalino y Ultracortex Headset para EEG 
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/m645BV.gif" width="50%">
  
  
### Tabla de contenidos
1. [Introducción](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#1-introducci%C3%B3n)
  
2. [Objetivos de la práctica de laboratorio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#2-objetivos-de-la-pr%C3%A1ctica-de-laboratorio)
  
3. [Materiales y equipos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#3-materiales-y-equipos)
  
4. [Procedimiento](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#4-procedimiento)
  
  
5. [Resultados](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#5-resultados)


6. [Discusión](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#6-discusi%C3%B3n)
  
7. [Conclusiones](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#7-conclusiones)
  
8. [Referencias](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Entregable%205.md#8-referencias)
  
### 1. Introducción
  El electroencefalograma (EEG) es un estudio que mide la actividad eléctrica en el cerebro mediante pequeños discos de metal (electrodos) colocados sobre el cuero cabelludo. Las neuronas cerebrales se comunican a través de impulsos eléctricos y están activas todo el tiempo, incluso mientras duermes. Esta actividad se manifiesta como líneas onduladas en un registro electroencefalográfico [1]
Un electroencefalograma es uno de los estudios principales para diagnosticar o tratar la epilepsia, encefalopatías, tumores cerebrales, accidentes cerebrovasculares, entre otros. [1]

### 2. Objetivos de la práctica de laboratorio
  - Adquirir señales biomédicas de EEG.
  - Hacer una correcta configuración de BiTalino y Ultracortex
  - Extraer la información de las señales ECG del software OpenSignals (r)evolution y OpenBCI GUI
  
### 3. Materiales y equipos
<div align="center">

|  **Imagen**  | **Producto** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="150" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg"> |   Kit BITalino  |       1      |
| <img width="200" height="150" src="https://www.pcspeed.com.pe/wp-content/uploads/2022/07/laptop-asus-rog-strix-g513ic-hn046w-amd-ryzen-7-4800h-16gb-512gb-ssd-t-video-rtx-3050-4gb-156-fhd-144hz-2.jpg"> |      Laptop     |       1      |
| <img width="200" height="250" src="https://cdn.shopify.com/s/files/1/0613/9353/products/DSC02861_900x.jpg?v=1652731236"> |      Ultracortex "Mark IV" EEG headset      |       1      | 
| <img width="200" height="250" src="https://cdn.shopify.com/s/files/1/0613/9353/products/DSC02779_900x.jpg?v=1614761059"> |      OpenBCI Cyton 8-channel Board      |       1      |
| <img width="200" height="250" src="https://user-images.githubusercontent.com/111662394/233752224-3bba27f3-377f-47e3-9191-3334f147efce.png"> |      Electrodos      |       1      |

</div>
</p>  
  
### 4. Procedimiento
Ubicar los electrodos según el Sistema Internacional de Posicionamiento 10/20, luego realizar los siguientes pasos:
- Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal, sin movimientos oculares/ojos cerrados) durante 30 segundos.
- Repetir un ciclo de ojos abiertos - ojos cerrados cinco veces, manteniendo ambas fases durante cinco segundos.
- Registrar otra fase de referencia de 30 segundos (paso 1).
- Un compañeros lee en voz alta una serie de ejercicios matemáticos [2] y quien tiene los electrodos resuelve cada uno de ellos mentalmente enfocando su     mirada en un punto específico para evitar artefactos (el tiempo entre pregunta y pregunta es de 12 segundos)
- Cubrir los ojos con un objeto por 60 segundos y luego realizar fotoestimulación con el flash de un celular (realizar barridos de lado a lado)

### 5. Resultados
---
  #### Conexión utilizada para ECG en BiTalino
  Se posicionaron los electrodos en base las guías mencionadas:
  
</p>
<p align="center">
  
  <img width="200" height="200" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Colocacion%20de%20electrodos%20Bitalino.png">
  
  Figura 2. Posición de los electrodos según la guía de Bitalino. [2]
  
  
  <img width="200" height="200" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Bitalino%20EEG.JPG">
  
  
  <img width="200" height="200" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Bitalino%20EEG%202.JPG">
</p>
<p align="center">
  
  #### Videos de ECG en BiTalino
  </p>

| Ojos cerrados | Intervalo 5 segundos ojos abiertos/ojos cerrados |
|:-------------:|:-------------:|
| <video src="https://user-images.githubusercontent.com/111662394/233754931-c9a684fc-7e02-4849-a4a8-a1949985ab3b.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/233755503-6f94f7fe-c1f0-48b7-8226-2329ed39e6d0.mp4" width="100" /> |
</div>











| Problema matemático | Flash luego de tener los ojos tapados|
|:-------------:|:-------------:|
| <video src="https://user-images.githubusercontent.com/111662394/233757053-bbe14db2-49b6-4898-bf49-29023e54d6b2.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/233757252-d2a2b67d-350c-4cf1-bf2d-aa650f22e1df.mp4" width="100" /> |
</div>
  
  
  #### Conexión utilizada para ECG en Ultracortex
  
</div>
</p>


### 6. Discusión
### 7. Conclusiones
### 8. Referencias
[1] “Electroencefalografía (EEG),” Mayo Clinic, 19-Jul-2022. [Online]. Available: https://www.mayoclinic.org/es-es/tests-procedures/eeg/about/pac-20393875. [Accessed: 21-Apr-2023]. 
[2]. https://bitalino.com/storage/uploads/media/homeguide3-eeg.pdf
