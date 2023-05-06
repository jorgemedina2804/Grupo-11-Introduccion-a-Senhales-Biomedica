# Laboratorio 7- Filtrado del dataset de ECG del laboratorio anterior
<p align="center">
  
<img src="https://user-images.githubusercontent.com/111662394/236525365-2e801efb-effd-4707-a1da-78575260ac83.png" width="50%">  

### Tabla de contenidos
  
1. [Introducción](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#1-introducci%C3%B3n)
2. [Objetivos de la práctica de laboratorio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#2-objetivos-de-la-pr%C3%A1ctica-de-laboratorio)
3. [Materiales y equipos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#3-materiales-y-equipos)
4. [Procedimiento](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#4-procedimiento)
5. [Resultados](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#5-resultados)
6. [Discusión](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#6-discusi%C3%B3n)
7. [Conclusiones](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#7-conclusiones)
8. [Referencias](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#8-referencias)

### 1. Introducción 
Un filtro es un dispositivo que discrimina, de acuerdo con algún atributo de los objetos aplicados a su entrada, lo que pasa a su través. En este caso, se hablará sobre filtros selectivos de frecuencia que dejan pasar señales con componentes de frecuencia en determinadas bandas mientras que atenúan señales que contienen frecuencias en otras bandas [1].
  
  Los filtros pueden ser divididos en dos grandes grupos: filtros analógicos y filtros digitales
  
   **Filtros analógicos**: Un filtro analógico es usado para señales en tiempo continuo, se pueden clasificar en filtros pasivos o activos de acuerdo al tipo de elementos que se utilizan [2]. Hay cuatro tipos básicos de filtros: 
  - **Filtro pasa-bajas:** permite el paso de todas las frecuencias menores a la 
    frecuencia de corte, atenuando aquellas que son mayores a esta última.
  - **Filtro pasa-altas:** atenúa todas las frecuencias bajas y permite el paso de 
    aquellas por encima de la frecuencia de corte.
  - **Filtro pasa-bandas:** deja pasar las frecuencias comprendidas entre 
    la frecuencia de corte inferior y la frecuencia de corte superior, atenuando las demás.
  - **Filtro rechaza-bandas:** atenúa las frecuencias comprendidas entre la 
    frecuencia de corte inferior y la frecuencia de corte superior, dejando pasar las demás [3]
  
  
  <p align="center">
  
  <img src="https://user-images.githubusercontent.com/111662394/236588405-fa6b201a-70a1-45f3-9b8f-a22d08961336.JPG" width="50%">  
  <p align="center">
   Fig 1. Representación gráfica de los filtros analógicos
   
   Los filtros activos se pueden clasificar, de acuerdo a la aproximación matemática empleada, en:
  - **Butterworth:** tiene objetivo una respuesta de ganancia plana en la banda de paso. Esto se consigue mediante una región de transición de caída lenta y una respuesta       de fase no lineal alrededor de la frecuencia de corte
  - **Chebyshev:** tiene como objetivo maximizar la pendiente de la característica de ganancia en la región de transición. Presenta un cierto rizado en la banda de paso,       que se incrementa al aumentar el orden de filtro.
  - **Bessel:** tiene como objetivo lograr una respuesta de fase lineal en un margen de frecuencias amplio en torno a la frecuencia de corte. La ganancia en la banda de         paso no es tan plana como en un filtro Butterworth ni la pendiente en la banda de transición tan acentuada como en un filtro Chebyshev
  - **Elíptica:** se caracteriza por tener ondulaciones constantes tanto en la banda de paso como en la banda de corte. [3]

  <p align="center">
  
  <img src="https://user-images.githubusercontent.com/111662394/236588834-b4c65400-2749-4f27-87e8-81b6a7be25fe.JPG" width="50%">  
  <p align="center">
   Fig 2. Comparación de los filtros analógicos activos

  
   #### Filtros digitales
    
Los filtros digitales son sistemas que operan sobre señales en tiempo discreto con el propósito de modificar el comportamiento en frecuencia de la señal. A diferencia de los filtros analógicos, los filtros digitales son fácilmente ajustables, y funcionan como soluciones software en un PC o hardware en dispositivos como DSPs o FPGAs. 

Dado que las señales de trabajo son discretas, los filtros digitales se modelan en el dominio Z, o a partir de una ecuación en diferencias. Si el sistema es lineal e invariante en el tiempo (LTI), el filtro digital se expresa utilizando la notación de ecuación en diferencias.

Los filtros digitales se dividen en filtros de respuesta al impulso finito (FIR: finite impulse response) y respuesta al impulso infinita (IIR: infinite impulse response). [4] 
 - **Filtros FIR:** produce una respuesta de salida finita en respuesta a una señal de entrada, y se llama FIR porque la respuesta se limita a un tiempo finito. A diferencia de otros filtros, los filtros FIR no tienen retroalimentación y solo operan en valores de entrada del pasado y del presente. La salida se genera a partir de una suma de un número limitado de muestras de la señal de entrada. Esta característica los hace muy estables y evita cualquier posible oscilación en la salida [5]
    
  <p align="center">
  
  <img src="https://user-images.githubusercontent.com/111662394/236589561-c86a5a91-a516-455c-9769-13701ab25f2e.JPG" width="50%">  
  
  
  <p align="center">
  Fig 3. Estructura de un filtro FIR 
   
  - **Filtros IIR:** generan una respuesta infinita en el tiempo en respuesta a una señal de entrada. A diferencia de los filtros FIR, estos filtros tienen una respuesta de impulso infinita y son recursivos, lo que significa que la salida depende tanto de la entrada actual como de las salidas anteriores (es decir, tiene retroalimentación) [6]
  
   <p align="center">
  
  <img src="https://user-images.githubusercontent.com/111662394/236589918-2670176e-6044-469f-a944-949b9034ec15.JPG" width="50%">  
  

  <p align="center">
  Fig 4. Estructura de un filtro IIR

    

    
### 2. Objetivos de la práctica de laboratorio 
  - Diseñar un filtro FIR usando el dataset de ECG obtenido el laboratorio pasado
  - Diseñar un filtro IIR usando el dataset de ECG obtenido el laboratorio pasado
  - Comparar la señal cruda con la señal filtrada.

### 3. Materiales y equipos
    
<div align="center">
    
|  **Imagen**  | **Producto/Programa** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="200" src="https://user-images.githubusercontent.com/111662394/236591622-748d54e3-5b66-49bc-8e8c-47df132ea7cf.png"> |   Python |       1      |
| <img width="200" height="200" src="https://www.pcspeed.com.pe/wp-content/uploads/2022/07/laptop-asus-rog-strix-g513ic-hn046w-amd-ryzen-7-4800h-16gb-512gb-ssd-t-video-rtx-3050-4gb-156-fhd-144hz-2.jpg"> |      Laptop     |       1      |

</div>
</p>   

### 4. Procedimiento

Se sigue el procedimiento establecido por la guía del laboratorio 7 proporcionada por el curso: 

  1. Se realiza la creación de las señales en Python 
  2. Se realiza la transformada rápida de Fourier para pasar la señal al dominio de la frecuencia 
  3. Se calcula la frecuencia de corte deseada
  4. Se diseña un filtro pasa baja ya sea FIR o IIR 
  5. Se realiza la transformada bilineal de H(s) a H(z)
  6. Se aplica el filtro a la señal de interés

Sin embargo también existe la alternativa de utilizar la librería recomendada para Bitalino para ser utilizada en Python. Si se desea más información sobre esta librería puede hacer uso del siguiente [link](https://github.com/pluxbiosignals/biosignalsnotebooks) y del siguiente [notebook](http://notebooks.pluxbiosignals.com/notebooks/Categories/Pre-Process/digital_filtering_filtfilt_rev.html )

### 5. Resultados

| Campo | Señal Cruda | Filtro Notch | Filtro  | Filtro |
|----------|----------|----------|----------|----------|
| Basal    | <img width="300" height="150" src=""> |  <img width="300" height="150" src="">    | <img width="300" height="150" src="">     | <img width="300" height="150" src="">     |
| Post-Ejercicio    | <img width="300" height="150" src="">  |       <img width="300" height="150" src="">        |       <img width="300" height="150" src="">           |       <img width="300" height="150" src="">           |
| Respiracion   | <img width="300" height="150" src="">  |       <img width="300" height="150" src="">        |       <img width="300" height="150" src="">           |       <img width="300" height="150" src="">           |


### 6. Discusión

Una de las importancias de analizar un ECG en el dominio del tiempo es más eficaz desde la perspectiva electrónica, computacional y algorítmica. La señal de ECG tiene un espectro frecuencial que va desde 0 a 100Hz

<p align="center">
<img src="https://user-images.githubusercontent.com/111662394/236633822-67f601bd-8823-4493-bf9b-c8a83417ddce.JPG" width="50%">

<p align="center">
Fig 5. Espectro de la señal ECG, ruido de línea de potencia eléctrica y de la señal compuesta por la suma de ambas señales. 

<p align="center">
Fig 6. Amplitud de rango de frecuencias de algunas señales biomedicas
  
Otra de las ventajas de analizar una señal en el dominio de la frecuencia es que es más fácil reconocer interferencias o ruidos no deseados. La siguiente imagen muestra las interferencias más comunes en un ECG las cuales son el movimiento, ruido muscular o por la corriente eléctrica.

  
<p align="center">
<img src="https://user-images.githubusercontent.com/111662394/236633897-16a83d67-629d-4a9f-9029-f8a076f76c0c.jpeg" width="50%">

<p align="center">
Fig 7. Espectro de frecuencias de una señal ECG, complejo QRS y algunos tipos de ruido

### 7. Conclusiones
### 8. Referencias  
    
[1].  J. G. Proakis and D. G. Manolakis, “5.4 Sistemas LTI como filtros de frecuencia,” in Tratamiento Digital De Señales, Madrid: Pearson Educación, 2009. 
[2]. “INTRODUCCIÓN A FILTROS ANALÓGICOS CAPÍTULO 1.” Available: http://catarina.udlap.mx/u_dl_a/tales/documentos/lem/torres_d_ld/capitulo1.pdf
    
[3]. A, Perez Garcia et al. (2014) Instrumentación Electrónica. Madrid: Paraninfo. 
    
[4]. D, Ballesteros & D,Torres (2018) Introducción a los filtros digitales. EE.UU: Redipe.
    
[5]. “Electrónica II - Bioingeniería -1ra. Parte Filtros Analógicos” Disponible en: http://dea.unsj.edu.ar/pdselo/Apuntes/Filtros-analogicos-1ra-parte.pdf
    
[6].Roshni Y, “Difference Between FIR Filter and IIR Filter (with Comparison chart) - Circuit Globe,” Circuit Globe, Mar. 24, 2020. https://circuitglobe.com/difference-between-fir-filter-and-iir-filter.html (accessed May 05, 2023). 
