"""Librería: Pandas
Crea un DataFrame de ventas, lo filtra, agrupa y exporta."""
import os
import pandas as pd

SALIDA = "salida"


def main():
    os.makedirs(SALIDA, exist_ok=True)
    df = pd.DataFrame({
        "vendedor": ["Ana", "Luis", "Ana", "María", "Luis", "María"],
        "region": ["Norte", "Sur", "Norte", "Centro", "Sur", "Centro"],
        "ventas": [1200, 800, 1500, 900, 1100, 1300],
    })

    print("Primeras filas:\n", df.head(), "\n")
    print("Resumen estadístico:\n", df["ventas"].describe(), "\n")
    print("Ventas mayores a 1000:\n", df[df["ventas"] > 1000], "\n")

    por_vendedor = df.groupby("vendedor")["ventas"].sum().sort_values(ascending=False)
    print("Total por vendedor:\n", por_vendedor)

    ruta = os.path.join(SALIDA, "ventas_por_vendedor.csv")
    por_vendedor.to_csv(ruta)
    print(f"\nResultado exportado a {ruta}")


if __name__ == "__main__":
    main()
