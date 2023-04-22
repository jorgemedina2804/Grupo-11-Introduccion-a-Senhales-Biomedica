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
  
  </p>
<p align="center">
  
  <img width="400" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Imagen%20introduccion.JPG">
  <p align="center">
   Fig 1. Descripción general de un electroencefalograma. Fuente: Mayo Clinic

  En un EEG se pueden identificar varios tipos de ondas, que se clasifican según su frecuencia y amplitud. Los principales tipos de ondas en un EEG son:

  - Ondas theta: son ondas de frecuencia intermedia que se observan durante el sueño ligero y en algunas condiciones patológicas, como en casos de lesiones       cerebrales o trastornos del sueño.
  - Ondas alfa: son ondas de frecuencia media que se observan en la corteza cerebral en estado de reposo y relajación, con los ojos cerrados.
  - Ondas beta: son ondas de alta frecuencia y baja amplitud que se observan en la corteza cerebral en estado de alerta, atención y actividad mental.
  - Ondas gamma: son ondas de alta frecuencia y baja amplitud que se observan en la corteza cerebral durante procesos cognitivos complejos y de percepción                 visual.
  - Ondas delta: son ondas de baja frecuencia y alta amplitud que se observan típicamente en adultos durante el sueño profundo y en niños pequeños en estado       de       vigilia.

 </p>
<p align="center">
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Ondas%20EEG.JPG">
  
  <p align="center">
  Fig 2. Ondas de EEG. Fuente: Sant Pau Centre Terapèutic
  
   Los electrodos deben ser posicionados siguiendo el sistema internacional 10/20 para así describir la localización de los electrodos en el usuario. Se le dice 10/20    debido a que al porcentaje (10 y 20) de distancia en la que deben estar colocados los electrodos en la parte frontal, occipital, de lado derecho e izquierda del        cráneo.
   Cada sitio tiene una letra para identificar el lóbulo y un número para identificar la ubicación del hemisferio [2]:
    
   - Electrodo F:Lóbulo Frontal
   - Electrodo T: Lóbulo Temporal
   - Electrodo C: Lóbulo Central 
   - Electrodo P: Lóbulo Parietal
   - Electrodo O: Lóbulo Occipital 
    
### 2. Objetivos de la práctica de laboratorio
  - Adquirir señales biomédicas de EEG.
  - Hacer una correcta configuración de BiTalino y Ultracortex
  - Extraer la información de las señales EEG del software OpenSignals (r)evolution y OpenBCI GUI
  
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
- Un compañeros lee en voz alta una serie de ejercicios matemáticos y quien tiene los electrodos resuelve cada uno de ellos mentalmente enfocando su     mirada en un punto específico para evitar artefactos (el tiempo entre pregunta y pregunta es de 12 segundos)
- Cubrir los ojos con un objeto por 60 segundos y luego realizar fotoestimulación con el flash de un celular (realizar barridos de lado a lado)

### 5. Resultados
---
  #### Conexión utilizada para EEG en BiTalino
  Se posicionaron los electrodos en base la guía de Bitalino [3]:
  
</p>
<p align="center">
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Colocacion%20de%20electrodos%20Bitalino.png">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Bitalino%20EEG.JPG">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Bitalino%20EEG%202.JPG">
  
</p>
<p align="center">
  
  #### Videos de EEG en BiTalino
  </p>

| Ojos cerrados | Intervalo 5 segundos ojos abiertos/ojos cerrados |
|:-------------:|:-------------:|
| <video src="https://user-images.githubusercontent.com/111662394/233754931-c9a684fc-7e02-4849-a4a8-a1949985ab3b.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/233755503-6f94f7fe-c1f0-48b7-8226-2329ed39e6d0.mp4" width="100" /> |
</div>


| Problema matemático | Flash luego de tener los ojos tapados|
|:-------------:|:-------------:|
| <video src="https://user-images.githubusercontent.com/111662394/233757053-bbe14db2-49b6-4898-bf49-29023e54d6b2.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/233757252-d2a2b67d-350c-4cf1-bf2d-aa650f22e1df.mp4" width="100" /> |
</div>
  
  ### Gráficas de EEG obtenidas de Open Signals ploteadas en Python
  </p>
<p align="center">
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/EEG%20Open%20Signals%2030%20segundos.jpeg">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/EEG%20Open%20Signals%20Intervalo%205%20segundos.jpeg">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/EEG%20Open%20Signals%20Ejercicio%20matematico.jpeg">
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/EEG%20Open%20Signals%20Flash.jpeg">
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/EEG%20Open%20Signals%20Repeticion%20paso%201.jpeg">
  
  ### Archivos en Python de EEG usando Bitalino 
- [Señal en Python para todos los ejercicios en Bitalino](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/bitalino_eeg.py)
</p>

  ### Archivos de datos de EEG usando Bitalino 
  - [Archivo de datos EEG cuando se cierra los ojos por 30 segundos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/1.%20EEG%2030%20segundos%20ojos%20cerrados%20.txt)
  - [Archivo de datos EEG cuando se abren y cierran los ojos en intervalos de 5 segundos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/2.%20Intervalos%205%20segundos.txt)
  - [Archivo de datos EEG cuando se hace la resolución de problemas matemáticos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/4.%20Ejercicio%20matematico.txt)
- [Archivo de datos EEG cuando se pasa un flash por los ojos luego de mantener los ojos vendados](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/5.%20Flash.txt)
- [Archivo de datos EEG repetición paso 1](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/3.%20Repeticion%20paso%201.txt)  
  
  #### Conexión utilizada para EEG en Ultracortex
  </p>
<p align="center">
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Posicion%20casco%20para%20EEG.jpg">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Casco%201.jpeg">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Casco%202.jpeg">
</p>
<p align="center">
  
</div>
</p>

#### Videos de EEG en OpenBCI GUI
  </p>

| Ojos cerrados | Intervalo 5 segundos ojos abiertos/ojos cerrados |
|:-------------:|:-------------:|
| <video src="https://user-images.githubusercontent.com/111662394/233791918-ce8af4fd-20f8-4cfa-ac58-97cef2478579.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/233792316-d629299e-3580-49fe-8c1a-083616e0440f.mp4" width="100" /> |
</div>

| Problema matemático 1 | Problema matemático 2|
|:-------------:|:-------------:|
| <video src="https://user-images.githubusercontent.com/111662394/233792491-ad66ba3c-f68f-411e-9552-94ac4c98cbf9.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/233792593-42a7f976-a05b-4c2d-a794-c6c504c41c1c.mp4" width="100" /> |
</div>

### Gráficas de EEG obtenidas de OpenBCI GUI ploteadas en Python
  </p>
<p align="center">
  
  <img width="300" height="300" src="">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Bitalino%20EEG.JPG">
  
  
  <img width="300" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%205/Bitalino%20EEG%202.JPG">



### 6. Discusión
En el primer experimento de los ojos cerrados en ambos casos (BiTalino y EEG headset) observamos que las ondas no se ven alteradas a lo largo de los 40 segundos de medicion, esto debido al estado constante  del sujeto de prueba. Las ondas observadas son de aproximadamente 8-12Hz que son consideradas ondas alfa.

En el segundo experimento las ondas en ambos caso, al pasar de ojos cerrados a ojos abiertos y viceversa, se ven ligeramente alteradas con picos superiores e inferiores con amplitud de aproximadamente el doble del estado basal, esto coincidiendo con el cambio de estado.

En el tercer caso mientras se le esta haciendo la pregunta al sujeto de prueba se observa que las ondas se mantienen en estado basal. Al momento de responder la pregunta las ondas en ambos casos se ven alteradas considerablemente en cuanto a amplitud y frecuencia lo cual representa un cambio en la alteracion cerebral mas intensa en comparacion a las anteriores.

En el cuarto experimento realizado solo para para el caso del bitalino mientras el sujeto esta con los ojos completamente tapados se observa un estado basal constante, el cual se ve alterado al momento de retirar la benda y exposicion al flash. Este es un cambio sumamente notorio en la amplitud y frecuencia, incluso superior al de las ondas mientras se estan respondiendo las preguntas. Esto pude ser debido al cambio repentino de exposicion a la luz ya que luego de unos segudos se observa que las ondas si bien no estan en estado basal, si se mantienen constantes con una frecuencia superior a las ondas alfa.

### 7. Conclusiones
  
Mediante las pruebas realizadas se pueden verificar que mediante estímulos sensitivos como la prueba de la luz o el abrir y cerrar los ojos se pasa del estado basal (ondas alpha) a un estado de concentracion (ondas beta)
También se puede ver cambios de ondas alpha a beta o gamma por preguntas cognitivas, esto se debe a que los lóbulos frontales y temporales, las cuales están relacionadas con la cognición y memoria, aumentan su actividad neuronal para las respuestas matemáticas mientras que en las pruebas sensitivas visuales se puede ver un aumenta de la actividad cerebral, específicamente del área sensitiva visual la cual se encuentra en el lóbulo parietal 
  
  
  
### 8. Referencias
[1] “Electroencefalografía (EEG),” Mayo Clinic, 19-Jul-2022. [Online]. Available: https://www.mayoclinic.org/es-es/tests-procedures/eeg/about/pac-20393875. [Accessed: 21-Apr-2023]. 
[2]. https://fisiologia.facmed.unam.mx/wp-content/uploads/2019/09/UTI-pr%C3%A1ctica-7-a.-Electroencefalograma.-AnexoManual.pdf
[3]. https://bitalino.com/storage/uploads/media/homeguide3-eeg.pdf
