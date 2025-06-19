import tkinter as tk
import random
from components.cell import Cell
from components.timer import Timer
from logic.score import Score
from logic.desafios import generar_desafio
from components.popup import mostrar_cartel_final

ROWS, COLS, MINAS = 6, 6, 8

class BuscaminasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Buscaminas Matemático")
        self.respuestas_correctas = 0

        self.timer = Timer(root)
        self.score = Score(root)
        self.matriz = [[False] * COLS for _ in range(ROWS)]
        self.celdas = {}

        self.colocar_minas()
        self.crear_tablero()
        self.timer.iniciar()

    def colocar_minas(self):
        colocadas = 0
        while colocadas < MINAS:
            x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
            if not self.matriz[x][y]:
                self.matriz[x][y] = True
                colocadas += 1

    def crear_tablero(self):
        for x in range(ROWS):
            for y in range(COLS):
                c = Cell(self, x, y)
                c.boton.grid(row=x + 2, column=y, padx=1, pady=1)
                self.celdas[(x, y)] = c

    def contar_minas_vecinas(self, x, y):
        return sum(
            self.matriz[nx][ny]
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if (dx or dy) and 0 <= (nx := x+dx) < ROWS and 0 <= (ny := y+dy) < COLS
        )

    def perder(self):
        self.timer.detener()
        mostrar_cartel_final(self.root, self.timer.segundos, self.respuestas_correctas)
