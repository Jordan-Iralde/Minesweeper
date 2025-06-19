import random

def crear_pregunta():
    tipo = random.choice(["ecuacion1", "logica"])

    if tipo == "ecuacion1":
        a = random.randint(1, 10)
        b = random.randint(0, 5)
        x = random.randint(1, 20)
        resultado = a * x + b
        return f"Resuelve: {a}x + {b} = {resultado}", x

    else:  # lógica numérica simple
        n = random.randint(10, 50)
        correcto = "sí" if n % 3 == 0 else "no"
        return f"¿El número {n} es múltiplo de 3?", correcto
