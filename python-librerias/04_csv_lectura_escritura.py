"""Librería: csv
Crea un archivo CSV de alumnos, lo lee y calcula el promedio de cada uno."""
import csv
import os

SALIDA = "salida"
ARCHIVO = os.path.join(SALIDA, "alumnos.csv")


def escribir_csv():
    os.makedirs(SALIDA, exist_ok=True)
    filas = [
        ["nombre", "matematicas", "ciencias", "historia"],
        ["Ana", 9, 8, 10],
        ["Luis", 7, 6, 8],
        ["María", 10, 9, 9],
    ]
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(filas)
    print(f"Archivo creado: {ARCHIVO}")


def leer_csv():
    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            notas = [int(fila[m]) for m in ("matematicas", "ciencias", "historia")]
            print(f"{fila['nombre']}: promedio {sum(notas) / len(notas):.2f}")


if __name__ == "__main__":
    escribir_csv()
    leer_csv()
