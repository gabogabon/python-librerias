"""Librería: fpdf (paquete fpdf2)
Genera un PDF con título, párrafo y una tabla sencilla."""
import os
from fpdf import FPDF

SALIDA = "salida"


def main():
    os.makedirs(SALIDA, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Reporte generado con FPDF", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, "Este PDF fue creado desde Python usando la libreria fpdf2. "
                         "Incluye un titulo, un parrafo y una tabla.")
    pdf.ln(5)

    datos = [("Producto", "Cantidad", "Precio"),
             ("Cuaderno", "10", "$25"),
             ("Lapiz", "50", "$5"),
             ("Mochila", "3", "$350")]
    for i, fila in enumerate(datos):
        pdf.set_font("Helvetica", "B" if i == 0 else "", 12)
        for celda in fila:
            pdf.cell(60, 10, celda, border=1)
        pdf.ln()

    ruta = os.path.join(SALIDA, "reporte_fpdf.pdf")
    pdf.output(ruta)
    print(f"PDF creado: {ruta}")


if __name__ == "__main__":
    main()
