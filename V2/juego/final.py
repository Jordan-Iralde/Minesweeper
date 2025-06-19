import tkinter as tk

def mostrar_mensaje(ventana, tiempo):
    popup = tk.Toplevel(ventana)
    popup.title("Fin del juego")
    tk.Label(popup, text="💥 Perdiste 💥", font=("Arial", 18), fg="red").pack(pady=10)
    tk.Label(popup, text=f"Tiempo: {tiempo} segundos", font=("Arial", 12)).pack()
    tk.Button(popup, text="Salir", command=ventana.quit).pack(pady=10)

def mostrar_ganaste(ventana, tiempo, aciertos):
    popup = tk.Toplevel(ventana)
    popup.title("¡Ganaste!")
    popup.geometry("260x160")
    popup.resizable(False, False)

    tk.Label(popup, text="🎉 ¡Ganaste! 🎉", font=("Arial", 18), fg="green").pack(pady=10)
    tk.Label(popup, text=f"⏱ Tiempo: {tiempo} segundos", font=("Arial", 12)).pack()
    tk.Label(popup, text=f"✅ Desafíos resueltos: {aciertos}", font=("Arial", 12)).pack()
    tk.Button(popup, text="Salir", command=ventana.quit).pack(pady=10)
