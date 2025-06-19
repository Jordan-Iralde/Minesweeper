import tkinter as tk

class Score:
    def __init__(self, root):
        self.valor = 0
        self.label = tk.Label(root, text="✅ 0 correctas", font=("Arial", 14))
        self.label.grid(row=1, column=0, columnspan=6)

    def actualizar(self, nuevo_valor):
        self.valor = nuevo_valor
        self.label.config(text=f"✅ {self.valor} correctas")
