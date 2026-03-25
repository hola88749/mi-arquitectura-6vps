import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import os

def excel_a_pdf(archivo_entrada):
    try:
        print(f"Leyendo el archivo: {archivo_entrada}...")

        # Leer Excel
        df = pd.read_excel(archivo_entrada)

        # Definir salida
        archivo_salida = archivo_entrada.replace(".xlsx", ".pdf")

        # Crear PDF
        pdf = SimpleDocTemplate(archivo_salida)

        # Convertir datos a lista
        data = [df.columns.tolist()] + df.values.tolist()

        # Crear tabla
        tabla = Table(data)

        # Estilo (para que se vea bien)
        estilo = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        tabla.setStyle(estilo)

        # Generar PDF
        pdf.build([tabla])

        print(" OK: PDF generado correctamente")
        print(f" Ruta: {os.path.abspath(archivo_salida)}")

    except Exception as e:
        print("❌ ERROR:", e)
