import tkinter as tk
import sys

def mostrar_mensaje(ventana, tiempo, gano=False):
    mensaje = (
        f"¡Ganaste en {tiempo} segundos!" if gano
        else f"Perdiste. Tiempo: {tiempo} segundos."
    )

    # Crear ventana de mensaje
    msg_win = tk.Toplevel(ventana)
    msg_win.title("Resultado")
    msg_win.geometry("300x100")
    msg_win.resizable(False, False)

    label = tk.Label(msg_win, text=mensaje, font=("Arial", 12))
    label.pack(expand=True, pady=20)

    # Cierra la ventana después de 5 segundos y finaliza el programa
    def cerrar_todo():
        ventana.quit()
        ventana.destroy()
        sys.exit()

    msg_win.after(3000, cerrar_todo)
