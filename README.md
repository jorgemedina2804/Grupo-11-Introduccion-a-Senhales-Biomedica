# Grupo 11 - Introducción a Señales Biomédicas
Bienvenidos al repositorio del grupo 11 del curso "Introducción a Señales Biomédicas" del ciclo 2023-1

## Nombre del proyecto: Detector semiautomático de arritmias de bajo costo utilizando la señal de ECG
## Project name: Low-cost semi-automatic arrhythmia detector using ECG signal




### Tabla de contenidos
- [Resumen](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#resumen)
- [Motivación](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#motivaci%C3%B3n)
- [Principales hallazgos](https://github.com/jorgemedina2804/Grupo-11-Introduccion-a-Senhales-Biomedica/tree/main#principales-hallazgos)

### Resumen:
<p align="justify">
Se realizará un dispositivo que sea capaz de analizar y realizar la detección semiautomática de arritmias a través de la señal de ECG. Se obtendrá, preprocesará y extraerá la información haciendo uso de los conocimientos proporcionados por el curso mediante el uso de Python.
<p align="justify">
El objetivo de este proyecto es poder proveer un sistema de bajo costo que pueda ser usado en los centros de salud de zonas rurales para realizar procedimientos predictivos de arritmias cardíacas a la población. Para esto se contará con un algoritmo de Machine Learning basado en el uso de autoencoders para así poder detectar anomalías en los latidos del corazón, los cuales serán adquiridos a través de un módulo AD8232 conectado a través de un Arduino UNO. 
<p align="justify">
Se cuenta con un LED verde que se encenderá una vez que el dispositivo se prende y un pulsador que permite a la persona que maneja el equipo activar el sistema para comenzar con la recolección de datos por un lapso de 5 segundos. Al momento que se comienza la recolección de datos un LED azul se encenderá indicando el correcto inicio del proceso, el cual se apagará una vez que se haya terminado la recolección de datos. Una vez realizado esto se procederá a procesar la señal primero haciendo uso de filtros digitales y posteriormente se aplicará el algoritmo de Machine Learning, en este caso será el uso de autoencoders, el cual es una técnica que aprovecha las redes neuronales para la tarea de aprendizaje de representación. Una vez realizado esto, el proceso y el resultado es mostrado a través de una interfaz gráfica de usuario (GUI) mediante una laptop. 




### Motivación:

### Principales hallazgos:
