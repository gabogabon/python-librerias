"""Librería: NumPy
Operaciones con arreglos, estadísticas y álgebra de matrices."""
import numpy as np


def main():
    a = np.array([1, 2, 3, 4, 5])
    print("Arreglo:", a)
    print("Cuadrados:", a ** 2)
    print("Media:", a.mean(), "| Desv. estándar:", round(a.std(), 3))

    print("linspace(0, 1, 5):", np.linspace(0, 1, 5))
    print("arange(0, 10, 2):", np.arange(0, 10, 2))

    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[5, 6], [7, 8]])
    print("Multiplicación de matrices:\n", m1 @ m2)
    print("Determinante de m1:", round(np.linalg.det(m1), 2))
    print("Inversa de m1:\n", np.linalg.inv(m1))

    # Resolver el sistema: 2x + y = 5 ; x + 3y = 10
    sol = np.linalg.solve(np.array([[2, 1], [1, 3]]), np.array([5, 10]))
    print("Solución del sistema (x, y):", sol)


if __name__ == "__main__":
    main()
