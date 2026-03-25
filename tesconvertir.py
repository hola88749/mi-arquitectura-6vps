import os
from convertir import excel_a_pdf

archivo_prueba = "test.xlsx"

def test_conversion():
    resultado = {
        "status": "OK",
        "mensaje": "",
        "archivo_salida": ""
    }

    try:
        excel_a_pdf(archivo_prueba)
        salida = archivo_prueba.replace(".xlsx", ".pdf")

        if os.path.exists(salida):
            resultado["mensaje"] = "Conversión exitosa"
            resultado["archivo_salida"] = salida
        else:
            resultado["status"] = "ERROR"
            resultado["mensaje"] = "No se generó el PDF"

    except Exception as e:
        resultado["status"] = "ERROR"
        resultado["mensaje"] = str(e)

    return resultado


if __name__ == "__main__":
    respuesta = test_conversion()
    print(respuesta)
