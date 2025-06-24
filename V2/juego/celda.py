import tkinter as tk
from tkinter import simpledialog
from logica.desafio import crear_pregunta
from juego.final import mostrar_mensaje

# Constantes visuales
MINA_ICONO = "💣"
COLOR_MINA = "red"
COLOR_SEGURO = "#d0ffd0"
FUENTE = ("Arial", 12)

class Celda:
    def __init__(self, ventana, fila, col, es_mina, minas, tiempo, todas_celdas=None):
        self.fila = fila
        self.col = col
        self.es_mina = es_mina
        self.minas = minas
        self.tiempo = tiempo
        self.todas_celdas = todas_celdas
        self.revelada = False

        self.boton = tk.Button(
            ventana, width=5, height=2, font=FUENTE, command=self.revelar
        )

    def contar_minas_alrededor(self):
        """Cuenta las minas alrededor de esta celda."""
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x, y = self.fila + dx, self.col + dy
                if (x, y) in self.minas:
                    total += 1
        return total

    def mostrar_numero(self):
        """Revela el número de minas cercanas."""
        numero = self.contar_minas_alrededor()
        self.boton.config(text=str(numero), bg=COLOR_SEGURO, state="disabled")
        self.revelada = True

    def chequear_ganador(self):
        """Verifica si todas las minas fueron reveladas correctamente (ganaste)."""
        for celda in self.todas_celdas:
            if celda.es_mina and not celda.revelada:
                return False
        self.tiempo.detener()
        mostrar_mensaje(self.boton.master, self.tiempo.segundos, gano=True)
        return True

    def revelar(self):
        """Revela la celda, preguntando si es mina o mostrando el número de minas alrededor."""
        if self.revelada:
            return  # Evitar múltiples clics

        if self.es_mina:
            pregunta, respuesta = crear_pregunta()
            entrada = simpledialog.askstring("Pregunta", pregunta)
            if entrada != str(respuesta):
                self.boton.config(text=MINA_ICONO, bg=COLOR_MINA, fg="white")
                self.revelada = True
                self.tiempo.detener()
                mostrar_mensaje(self.boton.master, self.tiempo.segundos)
                return exit
            else:
                self.mostrar_numero()
        else:
            self.mostrar_numero()

        # Verificar si ganó el jugador después de revelar
        self.chequear_ganador()
