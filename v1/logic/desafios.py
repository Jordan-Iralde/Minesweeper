import random

def generar_desafio():
    tipo = random.choice(["ecuacion", "cuenta", "logica"])

    if tipo == "ecuacion":
        x = random.randint(1, 9)
        a, b = random.randint(1, 5), random.randint(1, 10)
        r = a * x + b
        return f"Resuelve: {a}x + {b} = {r}", x

    elif tipo == "cuenta":
        a, b = random.randint(10, 40), random.randint(2, 9)
        c = (a + b) * random.randint(2, 5)
        return f"¿Cuánto es ({a} + {b}) * {c // (a + b)}?", c

    else:
        n = random.randint(10, 30)
        correcto = "sí" if n % 2 == 0 else "no"
        return f"¿El número {n} es par?", correcto
