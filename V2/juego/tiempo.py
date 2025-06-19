import tkinter as tk

class Tiempo:
    def __init__(self, ventana):
        self.segundos = 0
        self.ventana = ventana
        self.label = tk.Label(ventana, text="Tiempo: 0s", font=("Arial", 14))
        self.activo = True

    def mostrar(self):
        self.label.grid(row=0, column=0, columnspan=5)
        self.contar()

    def contar(self):
        if self.activo:
            self.segundos += 1
            self.label.config(text=f"Tiempo: {self.segundos}s")
            self.ventana.after(1000, self.contar)

    def detener(self):
        self.activo = False
