import numpy as np
import random
import os

def ruta_zigzag_vertical_t1():
    camino = []
    for j in range(20):
        if j % 2 == 0:
            for i in range(20):
                camino.append((i, j))
        else:
            for i in range(19, -1, -1):
                camino.append((i, j))
    return camino

def ruta_espiral_t2():
    camino = []
    for capa in range(10):
        top = capa
        bottom = 19 - capa
        left = capa
        right = 19 - capa
        for i in range(top, bottom + 1):
            camino.append((i, right))
        for j in range(right - 1, left - 1, -1):
            camino.append((bottom, j))
        for i in range(bottom - 1, top - 1, -1):
            camino.append((i, left))
        for j in range(left + 1, right):
            camino.append((top, j))
    return camino

def ruta_zigzag_horizontal_t3():
    camino = []
    for i in range(19, -1, -1):
        if (19 - i) % 2 == 0:
            for j in range(20):
                camino.append((i, j))
        else:
            for j in range(19, -1, -1):
                camino.append((i, j))
    return camino

def ruta_zigzag_vertical_t4():
    camino = []
    for j in range(19, -1, -1):
        if (19 - j) % 2 == 0:
            for i in range(19, -1, -1):
                camino.append((i, j))
        else:
            for i in range(20):
                camino.append((i, j))
    return camino


def generate_matriz():
    matriz = np.array([["00000"]*20]*20)
    return matriz

def parse_celda(valor):
    v_str = str(valor).replace(" ", "").replace(",", "")
    distancia = int(v_str[1:3])
    tiempo = int(v_str[3:])
    return distancia, tiempo

def generar_matriz_aleatoria():
    matriz = generate_matriz()
    puntos_cardinales = ['N', 'S', 'E', 'O']
    for i in range(20):
        for j in range(20):
            c = random.choice(puntos_cardinales)
            d = random.randint(10, 20)
            t = random.randint(1, 9)
            matriz[i, j] = f"{c}{d}{t}"
    return matriz

def cargar_matriz_archivo(ruta=None):
    matriz = generate_matriz()
    carpeta_actual = os.path.dirname(os.path.abspath(__file__)) 
    # Profe: aqui detectamos el sistema operativo para usar la ruta correcta.
    # En Windows usamos la ruta D:\municipio.txt, en Mac/Linux la carpeta del script.
    if ruta is None:
        if os.name == 'nt':  # 'nt' = Windows
            ruta = "D:\\municipio.txt"
        else:  # Mac (posix) o Linux
            ruta = os.path.join(carpeta_actual, "municipio.txt")
    rutas_candidatas = [ruta, "municipio.txt", os.path.join(carpeta_actual, "municipio.txt")]
    for ruta_actual in rutas_candidatas:
        try:
            with open(ruta_actual, 'r') as f:
                lineas = f.readlines()
                for i, linea in enumerate(lineas):
                    if i < 20:
                        datos = linea.strip().split(',')
                        for j in range(min(20, len(datos))):
                            matriz[i, j] = datos[j].strip()
            print(f"Datos cargados correctamente desde archivo: {ruta_actual} [9].")
            return matriz
        except FileNotFoundError:
            continue
    print("Archivo no encontrado en ninguna ruta. Generando matriz aleatoria de respaldo...")
    return generar_matriz_aleatoria()

def calcular_estadisticas_ruta(matriz, camino, destino_x, destino_y):
    tiempo_total = 0
    distancia_total = 0
    camino_recorrido = []

    for (i, j) in camino:
        camino_recorrido.append((i, j))
        d, t = parse_celda(matriz[i, j])
        distancia_total += d
        tiempo_total += t
        if i == destino_x and j == destino_y:
            break

    combustible = distancia_total / 6.0
    return tiempo_total, distancia_total, combustible, camino_recorrido

def mostrar_grafico_emoji(camino_recorrido, destino_x, destino_y):
    print("\nVisualización de la ruta óptima:")
    for i in range(20):
        fila_str = ""
        for j in range(20):
            if i == destino_x and j == destino_y:
                fila_str += "🧍"
            elif (i, j) in camino_recorrido:
                fila_str += "🚕"
            else:
                fila_str += "⬜"
        print(fila_str)


def main():
    matriz = generate_matriz()
    datos_cargados = False

    nombres_terminales = ['T1 (0,0)', 'T2 (0,19)', 'T3 (19,0)', 'T4 (19,19)']
    caminos_terminales = [
        ruta_zigzag_vertical_t1(),
        ruta_espiral_t2(),
        ruta_zigzag_horizontal_t3(),
        ruta_zigzag_vertical_t4()
    ]

    while True:
        print("\n*** Menú de SIMULACIÓN *** [9, 11, 12]")
        print("1.- Carga de Datos Aleatoria")
        print(r"2.- Carga desde un Archivo txt (D:\municipio.txt)")
        print("3.- Mostrar Información almacenada en la Matriz")
        print("4.- Indicar coordenadas (x,y) del Cliente y mostrar mejor terminal")
        print("5.- Indicar consumo de combustible por terminal hacia cliente")
        print("6.- Tiempo de recorrido completo de una Terminal a las otras")
        print("7.- Guardar archivo de salida (G4ecorrido.txt)")
        print("8.- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            matriz = generar_matriz_aleatoria()
            datos_cargados = True
            print("\nMatriz generada aleatoriamente.")

        elif opcion == '2':
            matriz = cargar_matriz_archivo()
            datos_cargados = True

        elif opcion == '3':
            if datos_cargados:
                print("\nMatriz del Municipio (20x20):")
                for i in range(20):
                    fila = [str(matriz[i, j]) for j in range(20)]
                    print("\t".join(fila))
            else:
                print("\nDebe cargar los datos primero (Opción 1 o 2).")

        elif opcion == '4' or opcion == '5':
            if not datos_cargados:
                print("\nDebe cargar los datos primero.")
                continue

            try:
                x = int(input("Ingrese coordenada X del cliente (0-19): "))
                y = int(input("Ingrese coordenada Y del cliente (0-19): "))

                if x < 0 or x > 19 or y < 0 or y > 19:
                    print("Coordenadas fuera de rango.")
                    continue

                tiempos = []
                distancias = []
                combustibles = []
                mejor_terminal = ""
                menor_tiempo = float('inf')
                mejor_camino = []

                for k in range(len(nombres_terminales)):
                    t_tot, d_tot, comb_tot, cam_real = calcular_estadisticas_ruta(matriz, caminos_terminales[k], x, y)
                    tiempos.append(t_tot)
                    distancias.append(d_tot)
                    combustibles.append(comb_tot)

                    if t_tot < menor_tiempo:
                        menor_tiempo = t_tot
                        mejor_terminal = nombres_terminales[k]
                        mejor_camino = cam_real

                if opcion == '4':
                    print("\n--- Resultados de Tiempos --- [12]")
                    for k in range(len(nombres_terminales)):
                        print(f"{nombres_terminales[k]}: {tiempos[k]} minutos")
                    print(f"\n> LA MEJOR TERMINAL ES {mejor_terminal} con {menor_tiempo} minutos.")
                    mostrar_grafico_emoji(mejor_camino, x, y)

                if opcion == '5':
                    print("\n--- Resultados de Combustible --- [12]")
                    for k in range(len(nombres_terminales)):
                        print(f"{nombres_terminales[k]}: Distancia = {distancias[k]} Km | Combustible consumido = {combustibles[k]:.2f} L")
            except ValueError:
                print("Por favor, ingrese valores enteros válidos.")

        elif opcion == '6':
            if not datos_cargados:
                print("\nDebe cargar los datos primero.")
                continue

            print("\nTerminales disponibles:")
            for idx in range(len(nombres_terminales)):
                print(f"{idx+1}. {nombres_terminales[idx]}")

            try:
                sel = int(input("Seleccione la terminal de salida (1-4): ")) - 1
                term_origen = nombres_terminales[sel]
                camino_origen = caminos_terminales[sel]

                coord_terminales = [(0,0), (0,19), (19,0), (19,19)]

                print(f"\nTiempos desde {term_origen} hacia los demás: [11, 12]")
                for dest_x, dest_y in coord_terminales:
                    if f"({dest_x},{dest_y})" not in term_origen:
                        t_tot, _, _, _ = calcular_estadisticas_ruta(matriz, camino_origen, dest_x, dest_y)
                        print(f"Hacia la terminal ({dest_x},{dest_y}): {t_tot} minutos")
            except (ValueError, IndexError):
                print("Selección inválida.")

        elif opcion == '7':
            if not datos_cargados:
                print("\nDebe cargar los datos primero.")
                continue

            with open('G4recorrido.txt', 'w') as f:
                for i in range(20):
                    for j in range(20):
                        d, t = parse_celda(matriz[i, j])
                        f.write(f"{d},{t}\n")
            print("\nArchivo 'G4recorrido.txt' generado exitosamente. [11]")

        elif opcion == '8':
            print("\nSaliendo del programa... [11]")
            break

        else:
            print("\nOpción inválida, intente de nuevo. [11]")

main()
