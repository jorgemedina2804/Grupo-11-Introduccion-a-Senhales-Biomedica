# Entregable 4 - Uso de BiTalino para ECG
<p align="center">
<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/ECG%20gif.gif" width="50%">


### Tabla de contenidos
1. [Introducción](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#1-introducci%C3%B3n)
2. [Objetivos de la práctica de laboratorio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#2-objetivos-de-la-pr%C3%A1ctica-de-laboratorio)
3. [Materiales y equipos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#3-materiales-y-equipos)
4. [Procedimiento](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#4-procedimiento)
5. [Resultados](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#5-resultados)
     
     5.1 [Conexión utilizada](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#conexi%C3%B3n-utilizada)
     5.2 [Videos de la señal obtenidas en OpenSignals](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#videos-de-la-se%C3%B1al-obtenidas-en-opensignals)
  
     5.3 [Ploteo de la señal en OpenSignals](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#ploteo-de-la-se%C3%B1al-en-opensignals)
  
     5.4 [Señal haciendo uso del ProSlim 4 Vital Sign Patient Simulator](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#se%C3%B1al-haciendo-uso-del-proslim-4-vital-sign-patient-simulator)
  
     5.5 [Ploteo de la señal en Python](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#ploteo-de-la-se%C3%B1al-en-python)
  
     5.6 [Archivos en Python](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#archivos-en-python)
  
     5.7 [Archivos de datos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#archivos-de-datos)
  
6. [Conclusiones](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#6-conclusiones)
7. [Referencias](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Entregable4.md#7-referencias)

### 1. Introducción
---
  <p align="justify">
  El ECG es un gráfico en el que se muestran las diferencias de voltaje en relación al tiempo, así como la actividad eléctrica del corazón que se desarrolla en el    corazón durante un tiempo determinado (normalmente no suele pasar de 30 segundos). La actividad eléctrica del corazón recogida en el ECG se observa en forma de un trazado que presenta diferentes deflexiones (ondas del ECG) que se corresponden con el recorrido de los impulsos eléctricos a través de las diferentes estructuras del corazón, como sabemos en corazón posee 2 nodos, el nodo SA y AV, que están encargados de la autorritmicidad del corazón. La despolarizacion de los muscúlos cardiacos comienzan en el nodo SA y se trasladada, primero a las aurículas, y luego al nodo AV donde posteriormente se dirige al haz de His (rama izquierda y derecha), para luego llegar a las paredes del ventrículo y toda la estructura del corazón mediante las fibras de Purkinje.
    
<p align="center">
   <img width="500" height="300" src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/Electrocardiograma-con-sus-ondas-intervalos-segmentos-y-su-relacion-con-el-ciclo.png">
<p align="center">
   Fig 1. ECG con sus respectivas ondas [1]
    
      
  <p align="justify">
  Las ondas que se pueden ver en un ECG son la onda P que describe la despolarización de la aurículas que expulsan la sangre a hacía las ventrículas, luego la onda QRS que describe la despolarización ventricular como también la polarización auricular en este periodo la presión ventricular excede a las presiones de las arterias aorta y tronco pulmonar lo que genera que la sangre sea expulsada hacia al resto del cuerpo y hacia los pulmones,respectivamente , luego el segmento ST que describe el periodo de meseta o de relajación isovolumétrica de los ventrículos y por último la onda T que describe la polarización ventricular es decir la disminución de la presión ventricular lo que genera que las valvulas del corazón se abran, por último hay un periodo de relajación que representa el llenado ventricular, ya que las válvulas están abiertas en ese momento.
  <p align="justify">
  La realización de un ECG es sencillo, un enfermero, un técnico o un médico le colocarán un total de 10 parches (electrodos). Se coloca uno en cada extremidad, formando así las seis derivaciones llamadas de los miembros. Los restantes seis parches se colocan en seis puntos específicos del pecho en la denominada región precordial, y hacen referencia a las seis derivaciones precordiales. Una derivación electrocardiográfica está constituida por la unión de dos electrodos.
    <p align="justify">
De esta forma, es posible conseguir un total de 12 derivaciones. Cada una permite obtener una visión electrocardiográfica diferente, representando 12 ventanas o puntos de observación distintos. Así, una anomalía que afecta a una parte concreta del corazón puede no ser advertida desde una derivación (ventana) y sí desde otra. Esta característica confiere valor al ECG para localizar la zona del corazón que puede encontrarse dañada. Cada derivación presenta un patrón del ECG característico con el que el médico está familiarizado, pero los principios expuestos en la descripción del ECG son aplicables a todas las derivaciones.[2]
      
      
#### ¿Cómo interpretar un ECG?  
      
### 2. Objetivos de la práctica de laboratorio
---
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino
- Extraer la información de las señales ECG del software OpenSignals (r)evolution
### 3. Materiales y equipos
---
  <div align="center">

|  **Imagen**  | **Producto** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="150" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg"> |   Kit BITalino  |       1      |
| <img width="200" height="150" src="https://www.pcspeed.com.pe/wp-content/uploads/2022/07/laptop-asus-rog-strix-g513ic-hn046w-amd-ryzen-7-4800h-16gb-512gb-ssd-t-video-rtx-3050-4gb-156-fhd-144hz-2.jpg"> |      Laptop     |       1      |
| <img width="200" height="250" src="https://www.flukebiomedical.com/sites/default/files/styles/slideshow_image/public/prosim4front_0.png"> |      ProSim 4 Vital Sign Patient Simulator     |       1      |
</div>

### 4. Procedimiento
---
Se utilizó la guía proporcionada por el curso respecto al uso de Bitalino para medir señales de ECG, junto con la hoja de datos y el manual de usuario. Además se realizó la toma de datos de la señal ECG en 3 momentos distintos: 
- Estado de reposo
- Aguantando la respiración por 10 segundos
- Luego de haber realizado ejercicio físico
### 5. Resultados
---
  #### Conexión utilizada
Se posicionaron los electrodos en base las guías mencionadas:
<p align="center"><img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/Electrodos%20en%20usuario.JPG" width="400" height="400">


  #### Videos de la señal obtenidas en OpenSignals
  | Estado Basal | Mantener la respiración por 10 segundos |
| ------------ |  :------------------------------------: |
| <video src="https://user-images.githubusercontent.com/111662394/232174327-5c1e784a-875e-4597-b174-80c180146a9b.mp4" width="200" /> | <video src="https://user-images.githubusercontent.com/111662394/232174661-61f3257b-a256-4d2d-a317-1dbb4e3f99ae.mp4" width="200" /> |
</div>

| Después de una actividad física   |        
| ------------ |  
|<video width="200"  src="https://user-images.githubusercontent.com/111662394/232174661-61f3257b-a256-4d2d-a317-1dbb4e3f99ae.mp4">|

  </div>

  #### Ploteo de la señal en OpenSignals
  | Estado Basal | Mantener la respiración por 10 segundos |
| ------------ |  :------------------------------------: |
| <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/Estado%20de%20reposo.JPG" width="500" /> | <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/10%20segundos.JPG" width="500" /> |
</div>


| Después de una actividad física   |        
| ------------ |  
|<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/Ejercicio.JPG" width="500"/>|
  #### Señal haciendo uso del ProSlim 4 Vital Sign Patient Simulator
| 30 latidos por minuto | 120 latidos por minuto |
| ------------ |  :------------------------------------: |
| <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/30%20lpm.JPG" width="500" /> | <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/120%20lpm.JPG" width="500" /> |


| 240 latidos por minuto | Arritmia Taquicárdica ventricular 200 latidos por minuto |
| ------------ |  :------------------------------------: |
| <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/240%20lpm.JPG" width="500" /> | <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/Arritmia%20Taq.JPG" width="500" /> |
  
  #### Ploteo de la señal en Python
  | Estado Basal | Mantener la respiración por 10 segundos |
  | ------------ |  :------------------------------------: |
  | <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/ECG%20Basal%20Python.jpeg" width="500" /> | <img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/ECG%2010%20segundos%20Python.jpeg" width="500" /> |
  </div>


| Después de una actividad física   |        
| ------------ |  
|<img src="https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Imagenes/ECG%20Actividad%20fisica%20Python.jpeg" width="500"/>|


  ### Archivos en Python
- [Señal brindada por los electrodos en el cuerpo ploteada en Python con un dominio de 3 segundos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/ploteo_ecg_seccionada_3seg.py)
- [Señal brindada por los electrodos en el cuerpo ploteada en Python con un dominio del tiempo completo de recopilación de señal](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/ploteo_ecg_completo.py)
- [Señal brindada por el ProSim 8 ploteada en Python con un dominio de 3 segundos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/ploteo_ecg_prosim_3seg.py)
</p>

  ### Archivos de datos
  - [Archivo de datos ECG estado basal](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/ECG%20tranquilo%20.txt)
  - [Archivo de datos ECG manteniendo la respiración durante 10 segundos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/ecg%2010%20segundos%20respiracion.txt)
  - [Archivo de datos ECG luego de realizar ejercicio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/ECG%20con%20ejercicio%20.txt)
  - [Archivo de datos ECG 30 lpm ProSim](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/30%20lpm%20pro%20sim.txt)
  - [Archivo de datos ECG 120 lpm ProSim](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/120%20lpm%20pro%20sim.txt)
  - [Archivo de datos ECG 240 lpm ProSim](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/240%20lpm%20pro%20sim.txt)
  - [Archivo de datos ECG Arritmia Taquicárdica ventricular 200 latidos por minuto ProSim](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%204/Arritmia%20Taq%20vent%20200%20lpm%20prosim.txt)
  
### 6. Conclusiones
---
### 7. Referencias
---
  [1]https://www.researchgate.net/figure/Electrocardiograma-con-sus-ondas-intervalos-segmentos-y-su-relacion-con-el-ciclo_fig2_333649418
  [2]https://www.fbbva.es/microsites/salud_cardio/mult/fbbva_libroCorazon_cap4.pdf
