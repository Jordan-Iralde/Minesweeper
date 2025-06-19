from tkinter import Tk
from juego.tablero import crear_tablero

# Crear ventana del juego
ventana = Tk()
ventana.title("Buscaminas Matemático")

# Llamar al tablero
crear_tablero(ventana)

# Mostrar ventana
ventana.mainloop()
