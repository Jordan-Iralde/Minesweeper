import tkinter as tk
from juego.celda import Celda
from juego.tiempo import Tiempo

FILAS = 5
COLUMNAS = 5
MINAS = 5

def crear_tablero(ventana):
    # Crear cronómetro arriba
    tiempo = Tiempo(ventana)
    tiempo.mostrar()

    # Crear tablero vacío
    minas = []
    botones = {}

    # Colocar minas al azar
    import random
    while len(minas) < MINAS:
        x, y = random.randint(0, FILAS-1), random.randint(0, COLUMNAS-1)
        if (x, y) not in minas:
            minas.append((x, y))

    # Crear botones sin pasar todas_celdas aún
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            tiene_mina = (fila, col) in minas
            celda = Celda(ventana, fila, col, tiene_mina, minas, tiempo, todas_celdas=None)
            celda.boton.grid(row=fila + 1, column=col)
            botones[(fila, col)] = celda

    # Ahora asignar todas_celdas (lista de todas las celdas) a cada celda
    todas_celdas = list(botones.values())
    for celda in todas_celdas:
        celda.todas_celdas = todas_celdas

