import tkinter as tk
from tkinter import simpledialog
from logic.desafios import generar_desafio

class Cell:
    def __init__(self, juego, x, y):
        self.juego = juego
        self.x = x
        self.y = y
        self.boton = tk.Button(juego.root, width=5, height=2, font=("Arial", 12),
                               bg="#f0f0f0", command=self.revelar)

    def revelar(self):
        if self.juego.matriz[self.x][self.y]:
            pregunta, respuesta = generar_desafio()
            entrada = simpledialog.askstring("Desafío", pregunta)
            if entrada and entrada.strip().lower() == str(respuesta).lower():
                self.juego.respuestas_correctas += 1
            else:
                self.boton.config(text="💣", bg="red", fg="white")
                self.juego.perder()
                return

        minas = self.juego.contar_minas_vecinas(self.x, self.y)
        self.boton.config(text=str(minas) if minas else "", bg="#d0ffd0", state="disabled")
