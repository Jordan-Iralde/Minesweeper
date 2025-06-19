import tkinter as tk
from tkinter import simpledialog

import random

# Tamaño del tablero
ROWS, COLS, MINES = 6, 6, 8

# Generador de desafíos complejos
def generar_desafio():
    tipo = random.choice(["ecuacion", "logica", "cuenta"])
    if tipo == "ecuacion":
        x = random.randint(1, 10)
        a, b = random.randint(1, 5), random.randint(1, 10)
        res = a * x + b
        return f"{a}x + {b} = {res}", x
    elif tipo == "cuenta":
        a, b, c = random.randint(1, 20), random.randint(1, 10), random.randint(1, 5)
        expr = f"({a} + {b}) * {c}"
        return expr + " = ?", eval(expr)
    else:  # lógica simple
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        pregunta = f"¿El número {a + b} es múltiplo de 3?"
        return pregunta, "sí" if (a + b) % 3 == 0 else "no"

# Componente de cartel
def mostrar_cartel_perdiste(root):
    popup = tk.Toplevel(root)
    popup.title("Fin del juego")
    popup.geometry("300x150")
    tk.Label(popup, text="💥 Perdiste 💥", font=("Arial", 18), fg="red").pack(pady=20)
    tk.Button(popup, text="Salir", command=root.destroy).pack()

# Lógica principal
class BuscaminasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Buscaminas Matemático")
        self.celdas = {}
        self.matriz = [[False for _ in range(COLS)] for _ in range(ROWS)]

        # Colocar minas
        for _ in range(MINES):
            while True:
                x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
                if not self.matriz[x][y]:
                    self.matriz[x][y] = True
                    break

        self.crear_tablero()

    def crear_tablero(self):
        for x in range(ROWS):
            for y in range(COLS):
                btn = tk.Button(self.root, width=6, height=3,
                                font=("Arial", 12), command=lambda i=x, j=y: self.revelar(i, j))
                btn.grid(row=x, column=y)
                self.celdas[(x, y)] = btn

    def contar_minas(self, x, y):
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and self.matriz[nx][ny]:
                    total += 1
        return total

    def revelar(self, x, y):
        btn = self.celdas[(x, y)]
        if self.matriz[x][y]:  # es mina → resolver desafío
            pregunta, respuesta = generar_desafio()
            entrada = simpledialog.askstring("Desafío Matemático", pregunta)
            if entrada is None or entrada.strip().lower() != str(respuesta).lower():
                btn.config(text="💣", bg="red", fg="white")
                mostrar_cartel_perdiste(self.root)
            else:
                minas = self.contar_minas(x, y)
                btn.config(text=str(minas), bg="lightgreen", state="disabled")
        else:
            minas = self.contar_minas(x, y)
            btn.config(text=str(minas) if minas > 0 else "", bg="lightgray", state="disabled")

# Ejecutar juego
if __name__ == "__main__":
    root = tk.Tk()
    app = BuscaminasApp(root)
    root.mainloop()
