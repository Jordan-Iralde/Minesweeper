import tkinter as tk
from tkinter import simpledialog
from logica.desafio import crear_pregunta
from juego.final import mostrar_mensaje

class Celda:
    def __init__(self, ventana, fila, col, es_mina, minas, tiempo, todas_celdas=None):
        self.fila = fila
        self.col = col
        self.es_mina = es_mina
        self.minas = minas
        self.tiempo = tiempo
        self.todas_celdas = todas_celdas
        self.boton = tk.Button(ventana, width=5, height=2, font=("Arial", 12), command=self.revelar)


    def contar_minas_alrededor(self):
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x, y = self.fila + dx, self.col + dy
                if (x, y) in self.minas:
                    total += 1
        return total

    def chequear_ganador(self):
        # Si no queda ninguna mina sin revelar -> ganaste
        for celda in self.todas_celdas:
            if celda.es_mina and celda.boton['text'] != "💣":
                # Queda al menos una mina no revelada
                return False
        # Si llegamos acá, ganaste
        self.tiempo.detener()
        mostrar_mensaje(self.boton.master, self.tiempo.segundos, gano=True)  # Podés agregar un parámetro para mostrar "ganaste"
        return True

    def revelar(self):
        if self.es_mina:
            pregunta, respuesta = crear_pregunta()
            entrada = simpledialog.askstring("Pregunta", pregunta)
            if entrada != str(respuesta):
                self.boton.config(text="💣", bg="red", fg="white")
                self.tiempo.detener()
                mostrar_mensaje(self.boton.master, self.tiempo.segundos)
                return
            else:
                # Si respondió bien, revelamos como si no fuera mina
                numero = self.contar_minas_alrededor()
                self.boton.config(text=str(numero), bg="#d0ffd0", state="disabled")
        else:
            numero = self.contar_minas_alrededor()
            self.boton.config(text=str(numero), bg="#d0ffd0", state="disabled")

        # Chequeamos si ganaste luego de revelar
        self.chequear_ganador()
