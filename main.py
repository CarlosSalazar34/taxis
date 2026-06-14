import numpy as np
from random import randint

def crear_matriz(matriz)->None:
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i, j] = randint(10, 20)

def main()->None:
    matriz = np.array([
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19,
        [0]*19
    ])
    crear_matriz(matriz=matriz)
    print(matriz)

if __name__ == "__main__":
    main()