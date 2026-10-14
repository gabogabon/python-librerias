"""Librería: math
Calcula potencias, raíces, factoriales y otras operaciones matemáticas."""
import math


def main():
    base, exponente = 2, 10
    print(f"{base} elevado a {exponente} = {math.pow(base, exponente):.0f}")
    print(f"Raíz cuadrada de 144 = {math.sqrt(144)}")
    print(f"Factorial de 6 = {math.factorial(6)}")
    print(f"Logaritmo natural de e^3 = {math.log(math.exp(3))}")
    print(f"Seno de 30° = {math.sin(math.radians(30)):.2f}")

    radio = 5
    print(f"Área de un círculo de radio {radio} = {math.pi * radio ** 2:.2f}")
    print(f"Hipotenusa de un triángulo 3-4 = {math.hypot(3, 4)}")


if __name__ == "__main__":
    main()
