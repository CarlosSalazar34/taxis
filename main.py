import numpy as np
from random import randint

def crear_matriz(matriz)->None:
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i, j] = randint(10, 20)

def movimiento_espiral_con_for(matriz) -> int:
    print("\n--- RECORRIDO EN ESPIRAL CON FOR ---")
    kilometros = 0
    n = len(matriz)
    
    # Calculamos el número de capas (para 19x19, n // 2 + n % 2 = 10 capas)
    capas = (n + 1) // 2
    
    # El FOR principal controla en qué "capa" o anillo exterior estamos trabajando
    for capa in range(capas):
        
        # 1. De izquierda a derecha (Fila superior de la capa actual)
        for j in range(capa, n - capa):
            print(matriz[capa, j], end=" -> ")
            kilometros += matriz[capa, j]
            
        # 2. De arriba a abajo (Columna derecha de la capa actual)
        for i in range(capa + 1, n - capa):
            print(matriz[i, n - capa - 1], end=" -> ")
            kilometros += matriz[i, n - capa - 1]
            
        # 3. De derecha a izquierda (Fila inferior de la capa actual)
        for j in range(n - capa - 2, capa - 1, -1):
            # Condición para evitar repetir celdas en el centro si la matriz fuera impar
            if n - capa - 1 != capa:
                print(matriz[n - capa - 1, j], end=" -> ")
                kilometros += matriz[n - capa - 1, j]
                
        # 4. De abajo a arriba (Columna izquierda de la capa actual)
        for i in range(n - capa - 2, capa, -1):
            # Condición para evitar repetir columnas en el centro
            if n - capa - 1 != capa:
                print(matriz[i, capa], end=" -> ")
                kilometros += matriz[i, capa]

    print("\n\n-> ¡Se completó el espiral usando ciclos FOR!")
    return kilometros


def calcular_vertical(matriz, nrows, ncols) -> int:
    print("\n--- RECORRIDO ZIG-ZAG VERTICAL ---")
    kilometros = 0
    for col in range(ncols - 1, -1, -1):
        if col % 2 == 0:
            rows = range(nrows - 1, -1, -1) 
        else:
            rows = range(0, nrows, 1)
            
        for row in rows:
            kilometros += matriz[row, col]
    return kilometros

def main()->None:
    matriz = np.array([
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20
    ])
    crear_matriz(matriz=matriz)
    print(matriz)
    total_vertical: int = calcular_vertical(matriz=matriz, nrows=len(matriz), ncols=len(matriz[0]))
    print(total_vertical)
if __name__ == "__main__":
    main()