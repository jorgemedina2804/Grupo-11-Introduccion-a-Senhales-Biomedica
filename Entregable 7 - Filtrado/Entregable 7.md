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
7.[Conclusiones] (https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Entregable%207.md#7-conclusiones)
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
  #### Estado basal

| Señal Cruda | Espectro de frecuencias previo al filtrado  |Espectro de fase previo al filtrado | 
|----------|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236637551-301802bb-95df-4b77-9d63-7b319fb933d5.png"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236645760-490bfce3-9249-4dee-ad58-b9d0bfad6881.JPG"> | <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236645797-03adc3da-67ea-43d9-abbe-45b809ae425e.JPG"> |

| Filtrado Normal con Pasabajas | Filtrado "filtfilt" | 
|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646083-1f569069-4ce9-47e7-b626-8ba862e95453.png"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646101-97d55bcd-75ed-41c6-958a-6b106ea79f6d.png"> | 

| Espectro de frecuencias post filtrado  |Espectro de fase post filtrado | 
|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646213-56e15138-a062-49cb-abe2-11d34db1378a.JPG"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646484-84e86aea-0a2a-4791-af87-859d8c9a8644.JPG"> |

<p align="center">
  
  <img src="https://user-images.githubusercontent.com/111662394/236647588-1b11a65f-8f14-4dba-bb28-87f8258509f7.png" width="80%" > 

  


  #### Ejercicio
  
  | Señal Cruda | Espectro de frecuencias previo al filtrado  |Espectro de fase previo al filtrado | 
|----------|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646576-0956aad1-b848-4ce4-9fed-f759e9527f59.JPG"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646624-93c49127-ad2e-4ce9-ad41-6653c67e931a.JPG"> | <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646670-fe8570de-5182-4049-99da-ea0eb0616265.JPG"> |

| Filtrado Normal con Pasabajas | Filtrado "filtfilt" | 
|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646705-49724c5c-f81b-4f5d-b61f-796f4c963505.png"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646879-5e3c681c-0ffb-4898-8d09-4e8aa161f72a.png"> | 

| Espectro de frecuencias post filtrado  |Espectro de fase post filtrado | 
|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646959-e241e742-5c5f-4b75-a130-113d5461f02d.JPG"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236646987-cf040ecb-0ad3-4068-b1df-7a50339219c7.JPG"> |
  
  #### Respiración
  
 | Señal Cruda | Espectro de frecuencias previo al filtrado  |Espectro de fase previo al filtrado | 
|----------|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647140-263cafa7-2e09-46cd-bb31-299affdf2d3d.png"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647199-e43a8883-d0a3-4eb9-83fa-ace9e70136c9.JPG"> | <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647234-52aa37f2-9361-44ca-96a7-2dbe06cac272.JPG"> |

| Filtrado Normal con Pasabajas | Filtrado "filtfilt" | 
|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647391-118f5ae8-14a0-4bfe-b211-522069ee5539.png"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647410-75d55915-1ee5-4074-b4f0-00e1bb6218b7.png"> | 

| Espectro de frecuencias post filtrado  |Espectro de fase post filtrado | 
|----------|----------|
| <img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647443-c2b1e51e-49d3-43d5-b1d1-6a44ec263160.JPG"> |<img width="500" height="500" src="https://user-images.githubusercontent.com/111662394/236647462-41c2c063-d116-4efb-9b32-43f97b690c3f.JPG"> |

<p align="center">
  
  <img src="https://user-images.githubusercontent.com/111662394/236647550-3a42b660-201c-4680-a42d-80d124568fab.JPG" width="50%">  









[Notebook Estado Basal](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Notebooks/Laboratorio_7_BASAL.ipynb)

[Notebook Ejercicio](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Notebooks/Laboratorio_7_Ejercicio.ipynb)

[Notebook Respiracion](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/Entregable%207%20-%20Filtrado/Notebooks/Laboratorio_7_Respiracion.ipynb)
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

  
En el espectro de frecuencias de nuestra señal ECG podemos ver una señal no común en el espectro de frecuencias de una ECG que tiene una frecuencia de 60Hz, la cual hemos identificado como una interferencia generada por corriente eléctrica

<p align="center">

<img src="https://user-images.githubusercontent.com/111662394/236634284-e20fa2f0-65ed-457b-aac4-70b6bb9a47ad.JPG" width="50%">

<p align="center">
Fig 8. Espectro de frecuencias adquiridas pre filtrado Notch en el caso de estado basal

### 7. Conclusiones    
La importancia de analizar una señal en el dominio de la frecuencia es que nos permite reconocer interferencias para poder ser eliminados por filtro de tipo FIR o IIR, en nuestro caso hemos concluido que el filtro IIR es más eficiente para poder eliminar interferencias en una señal ECG.

Los filtros digitales IIR frente a los FIR es que normalmente requieren menores coeficientes para hacer operaciones similares de filtrado. Por lo tanto, los filtros IIR se ejecutan más rápido y no requieren de memoria extra.

### 8. Referencias  
    
[1].  J. G. Proakis and D. G. Manolakis, “5.4 Sistemas LTI como filtros de frecuencia,” in Tratamiento Digital De Señales, Madrid: Pearson Educación, 2009. 
[2]. “INTRODUCCIÓN A FILTROS ANALÓGICOS CAPÍTULO 1.” Available: http://catarina.udlap.mx/u_dl_a/tales/documentos/lem/torres_d_ld/capitulo1.pdf
    
[3]. A, Perez Garcia et al. (2014) Instrumentación Electrónica. Madrid: Paraninfo. 
    
[4]. D, Ballesteros & D,Torres (2018) Introducción a los filtros digitales. EE.UU: Redipe.
    
[5]. “Electrónica II - Bioingeniería -1ra. Parte Filtros Analógicos” Disponible en: http://dea.unsj.edu.ar/pdselo/Apuntes/Filtros-analogicos-1ra-parte.pdf
    
[6].Roshni Y, “Difference Between FIR Filter and IIR Filter (with Comparison chart) - Circuit Globe,” Circuit Globe, Mar. 24, 2020. https://circuitglobe.com/difference-between-fir-filter-and-iir-filter.html (accessed May 05, 2023). 
