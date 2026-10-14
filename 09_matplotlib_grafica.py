"""Librería: Matplotlib
Genera una figura con una gráfica de línea y una de barras."""
import os
import matplotlib.pyplot as plt
import numpy as np

SALIDA = "salida"


def main():
    os.makedirs(SALIDA, exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

    x = np.linspace(0, 2 * np.pi, 100)
    ax1.plot(x, np.sin(x), label="seno")
    ax1.plot(x, np.cos(x), label="coseno")
    ax1.set_title("Funciones trigonométricas")
    ax1.legend()
    ax1.grid(True)

    meses = ["Ene", "Feb", "Mar", "Abr", "May"]
    ventas = [120, 150, 90, 180, 210]
    ax2.bar(meses, ventas, color="steelblue")
    ax2.set_title("Ventas mensuales")
    ax2.set_ylabel("Unidades")

    plt.tight_layout()
    ruta = os.path.join(SALIDA, "graficas.png")
    plt.savefig(ruta, dpi=120)
    print(f"Gráfica guardada en {ruta}")
    plt.show()


if __name__ == "__main__":
    main()
