"""Librería: random
Genera números aleatorios, mezcla listas, hace sorteos y crea contraseñas."""
import random
import string


def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(caracteres) for _ in range(longitud))


def main():
    random.seed(42)  # Semilla fija: los resultados se pueden repetir
    print("Entero entre 1 y 100:", random.randint(1, 100))
    print("Decimal entre 0 y 1:", round(random.random(), 4))

    participantes = ["Ana", "Luis", "María", "Carlos", "Sofía"]
    print("Ganador del sorteo:", random.choice(participantes))
    print("Tres elegidos sin repetir:", random.sample(participantes, 3))

    random.shuffle(participantes)
    print("Lista mezclada:", participantes)
    print("Contraseña generada:", generar_contrasena())


if __name__ == "__main__":
    main()
