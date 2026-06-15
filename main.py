import numpy as np
from random import randint

def crear_matriz(matriz)->None:
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i, j] = randint(10, 20)

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