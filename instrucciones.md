# Instrucciones para el Proyecto: Optimización Servicio Taxis (OST)

## 1. Descripción General
Se requiere desarrollar un programa en Python que simule y optimice las rutas de una línea de taxis ("La Excelencia") dentro de un municipio [1, 2]. El objetivo es determinar el menor tiempo y consumo de combustible para llegar a un cliente desde 4 terminales diferentes [3, 4]. 

## 2. Estructura de Datos
- El mapa del municipio se debe representar obligatoriamente como una **Matriz de 20 filas por 20 columnas** utilizando `numpy arrays` [4].
- Cada celda de la matriz representa una zona y contiene un valor de tipo String con el siguiente formato: `PuntoCardinal` + `Distancia` + `Tiempo` [5].
  - **Punto Cardinal:** `N` (Norte), `S` (Sur), `E` (Este) u `O` (Oeste) [5].
  - **Distancia:** Kilómetros de la zona, valor entre 10 y 20 [5].
  - **Tiempo:** Minutos que toma recorrer la zona, valor entre 1 y 9 [5].
  - *Ejemplo:* La celda `N128` indica Norte, 12 Km de distancia y 8 minutos de recorrido [5].

## 3. Terminales y Algoritmos de Recorrido
Existen 4 terminales ubicadas en las esquinas de la matriz, cada una con un algoritmo de recorrido **FIJO y ÚNICO** [6]:
- **Terminal 1 - (0, 0):** Recorrido en **Zigzag Vertical** [6].
- **Terminal 2 - (0, 19):** Recorrido en **Espiral** (en el sentido de las agujas del reloj) [6].
- **Terminal 3 - (19, 0):** Recorrido en **Zigzag Horizontal** [6].
- **Terminal 4 - (19, 19):** Recorrido en **Zigzag Vertical** [6].

## 4. Cálculos y Restricciones del Sistema
- **Tiempo estimado:** Sumatoria del tiempo en minutos de cada celda visitada hasta llegar al cliente [7].
- **Combustible:** Sumatoria de las distancias (Km) dividida entre el rendimiento fijo del taxi, el cual es de **6 kilómetros por 1 litro de combustible** [4].
- **Restricciones Técnicas:** Solo se permite el uso de arreglos de NumPy (`np.array`) e iteraciones convencionales (`for`, `while`). Se exige alta modularidad mediante el uso de **Funciones y Procedimientos** [8, 9]. El código debe estar documentado con comentarios [9].

## 5. Menú de Simulación Requerido
El programa debe ejecutarse bajo un menú infinito que solo se detenga al seleccionar la opción 8 [10]. Las opciones requeridas son:

1. **Carga de Datos Manual o Aleatoria:** Generar aleatoriamente los datos de las 400 celdas (20x20) [2, 11].
2. **Carga desde Archivo txt:** Leer una matriz predefinida desde el archivo `D:\municipio.txt` [2]. (Este archivo tiene 20 datos separados por comas por cada línea) [11].
3. **Mostrar Matriz:** Imprimir en consola la información almacenada actualmente en la matriz 20x20 [12].
4. **Solicitar Taxi (Mejor Tiempo):** 
   - Pedir al usuario las coordenadas `(x, y)` del cliente [12].
   - Calcular los tiempos desde las 4 terminales hasta el cliente e indicar **cuál es la mejor (menor tiempo)** [12].
   - **Salida Gráfica:** Mostrar la ruta ganadora de forma gráfica sobre una cuadrícula 20x20 usando **emojis** (ej. un taxi 🚕 para la ruta, y una persona 🧍 para el cliente) [13].
5. **Consumo de Combustible:** Dadas las coordenadas `(x, y)` del cliente, calcular y mostrar el consumo de combustible en litros para llegar desde cada una de las 4 terminales [12].
6. **Tiempo entre Terminales:** Pedir al usuario que elija una terminal de salida y mostrar el tiempo por separado que tarda en llegar a las otras 3 terminales usando su recorrido fijo [10, 12].
7. **Generar Archivo de Salida:** Crear un archivo llamado `recorrido.txt` que guarde la distancia y el tiempo de toda la matriz, con el formato estricto `Distancia,Tiempo` (Ejemplo: `12,5`), un dato por línea [10].
8. **Salir:** Finalizar el programa [10]. Si se ingresa cualquier otra opción en el menú, se debe regresar al inicio [13].

## 6. Normas de Entrega
Al finalizar, los entregables deben ser renombrados estrictamente de la siguiente manera:
- Archivo Python: `ApellidoGrupoN.py` (Ejemplo: `Holguingrupo7.py`) [14].
- Archivo de Texto generado en la opción 7: `GNrecorrido.txt` (Ejemplo: `G7recorrido.txt`) [14, 15].