import tkinter as tk

class Timer:
    def __init__(self, root):
        self.segundos = 0
        self.label = tk.Label(root, text="⏱️ 0s", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=6, pady=5)
        self.corriendo = False

    def iniciar(self):
        self.corriendo = True
        self._tick()

    def _tick(self):
        if self.corriendo:
            self.segundos += 1
            self.label.config(text=f"⏱️ {self.segundos}s")
            self.label.after(1000, self._tick)

    def detener(self):
        self.corriendo = False
