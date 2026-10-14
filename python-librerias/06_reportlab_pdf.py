"""Librería: reportlab
Genera una factura en PDF con texto y una tabla con estilos."""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

SALIDA = "salida"


def main():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, "factura_reportlab.pdf")
    estilos = getSampleStyleSheet()

    items = [["Descripción", "Cant.", "Precio", "Total"],
             ["Teclado", 2, 450, 900],
             ["Mouse", 3, 200, 600],
             ["Monitor", 1, 3200, 3200]]
    total = sum(fila[3] for fila in items[1:])
    items.append(["", "", "TOTAL", total])

    tabla = Table(items, colWidths=[200, 60, 80, 80])
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
    ]))

    doc = SimpleDocTemplate(ruta, pagesize=letter)
    doc.build([Paragraph("Factura de ejemplo", estilos["Title"]),
               Paragraph("Generada con la librería ReportLab.", estilos["Normal"]),
               Spacer(1, 20), tabla])
    print(f"PDF creado: {ruta}")


if __name__ == "__main__":
    main()
