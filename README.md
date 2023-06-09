# Grupo 11 - Introducción a Señales Biomédicas
Bienvenidos al repositorio del grupo 11 del curso "Introducción a Señales Biomédicas" del ciclo 2023-1

## Nombre del proyecto: Detector semiautomático de arritmias de bajo costo utilizando la señal de ECG
## Project name: Low-cost semi-automatic arrhythmia detector using ECG signal




### Tabla de contenidos
- [Resumen](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#resumen)
- [Motivación](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#motivaci%C3%B3n)
- [Principales hallazgos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#principales-hallazgos)
- [Referencia al entregable 1](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/README.md#referencia-al-entregable-1)
- [Referencias](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/README.md#referencias)

### Resumen:
<p align="justify">
Se realizará un dispositivo que sea capaz de analizar y realizar la detección semiautomática de arritmias a través de la señal de ECG. Se obtendrá, preprocesará y extraerá la información haciendo uso de los conocimientos proporcionados por el curso mediante el uso de Python.
<p align="justify">
El objetivo de este proyecto es poder proveer un sistema de bajo costo que pueda ser usado en los centros de salud de zonas rurales para realizar procedimientos predictivos de arritmias cardíacas a la población. Para esto se contará con un algoritmo de Machine Learning basado en el uso de autoencoders para así poder detectar anomalías en los latidos del corazón, los cuales serán adquiridos a través de un módulo AD8232 conectado a través de un Arduino UNO. 
<p align="justify">
Se cuenta con un LED verde que se encenderá una vez que el dispositivo se prende y un pulsador que permite a la persona que maneja el equipo activar el sistema para comenzar con la recolección de datos por un lapso de 5 segundos. Al momento que se comienza la recolección de datos un LED azul se encenderá indicando el correcto inicio del proceso, el cual se apagará una vez que se haya terminado la recolección de datos. Una vez realizado esto se procederá a procesar la señal primero haciendo uso de filtros digitales y posteriormente se aplicará el algoritmo de Machine Learning, en este caso será el uso de autoencoders, el cual es una técnica que aprovecha las redes neuronales para la tarea de aprendizaje de representación. Una vez realizado esto, el proceso y el resultado es mostrado a través de una interfaz gráfica de usuario (GUI) mediante una laptop. 




### Motivación:
<p align="justify">
Las arritmias cardíacas son trastornos del ritmo cardíaco que afectan a millones de personas en todo el mundo. Según la Organización Mundial de la Salud, las enfermedades cardiovasculares, incluyendo las arritmias, son la principal causa de muerte en todo el mundo, representando el 31% de todas las muertes [1]. En caso del Perú, el 17,49% de pacientes ingresados al servicio de cardiología de un hospital público del Perú padecen esta condición por lo que es importante prestar atención a la incidencia de arritmias cardíacas [2]. 
<p align="justify">
Se decidió concentrar a nuestro público objetivo en las zonas rurales debido a que el Perú ostenta un déficit de 6 mil 398 médicos especialistas, entre los que destacan la especialidad de cardiología [3]. Además, otro factor a tener en cuenta es el centralismo presente en el Perú, sobre todo en el sector salud. De cada diez médicos colegiados, seis se concentran en Lima y Callao. El 40% restante se distribuye también inequitativamente entre algunas regiones [4]. 

Ante todas estas evidencias es que se optó por realizar este proyecto. 


### Principales hallazgos:
<p align="justify">
Respecto a los hallazgos al término del proyecto, se pudo observar una especificidad del 80% en la obtención de los resultados del dispositivo, ya que al momento de ser probado en diferentes sujetos de prueba que cumplieron adecuadamente los requisitos necesarios para una adecuada toma de datos (mantenerse quietos durante la toma de datos y tener colocados los electrodos de manera correcta) el dispositivo funciona de manera correcta, detectando la presencia o ausencia de las arritmias cardíacas. Esto se da gracias al uso de la técnica de Machine Learning empleada, en este caso los autoencoders los cuales son redes neuronales utilizadas en el proyecto para que realicen un aprendizaje automático de la señal de electrocardiograma propia de una persona y de una persona que presenta algún tipo de arritmia cardíaca. 
<p align="justify">
Otro tema importante a recalcar es la velocidad con la que se puede conseguir la predicción de la arritmia cardíaca, ya que todo el proceso de recolección de la señal, procesamiento y análisis mediante Machine Learning dura menos de 1 minuto, con lo cual se logra el objetivo principal del proyecto el cual es ser poder obtener un dispositivo de bajo costo que pueda realizar la predicción de arritmias en corto tiempo para así poder emitir una primera alerta hacia un potencial paciente arrítmico. 


### Referencia al entregable 1:
[Entregable 1](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/blob/main/ISB/Laboratorios/L1_Sobre%20Nosotros/L1.md)

### Referencias:
[1]. “Cardiovascular diseases (CVDs).”https://www.who.int/news-room/fact-
sheets/detail/cardiovascular-diseases-(cvds) (accessed Jul.07, 2023)

[2]. D. Chambergo-Michilot, B. Velit-Rios, and A. Cueva-Parra, “Prevalencia de Enfermedades cardiovasculares en el hospital Nacional dos de Mayo de Perú,” Revista Mexicana de Angiología, vol. 48, no. 3, 2020. doi:10.24875/rma.20000012.

[3]. “Perú tiene un déficit de 6 mil 398 Médicos Especialistas,” RPP, https://rpp.pe/lima/actualidad/peru-tiene-un-deficit-de-6-mil-398-medicos-especialistas-noticia-840351?ref=rpp (accessed Jul. 5, 2023).

[4]. "La deficiente atención de salud en área rural,"" (JAIME MORÁN Secretario del Interior del Colegio Médico del Perú),
"https://revistaideele.com/ideele/content/la-deficiente-atención-de-salud-en-área-rural.
