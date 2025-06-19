import tkinter as tk

def mostrar_cartel_final(root, tiempo, aciertos):
    popup = tk.Toplevel(root)
    popup.title("🎉 Resultado")
    popup.geometry("260x160")
    popup.resizable(False, False)

    tk.Label(popup, text="💥 ¡Fin del juego! 💥", font=("Arial", 16), fg="blue").pack(pady=10)
    tk.Label(popup, text=f"⏱ Tiempo: {tiempo}s", font=("Arial", 12)).pack()
    tk.Label(popup, text=f"✅ Respuestas correctas: {aciertos}", font=("Arial", 12)).pack()

    tk.Button(popup, text="Salir", font=("Arial", 12), command=root.destroy).pack(pady=10)
