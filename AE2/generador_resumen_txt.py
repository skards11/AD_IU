from pathlib import Path
from datetime import datetime

class GeneradorResumenTXT:
    """Genera un resumen reproducible a partir de los resultados de las clases CSV y JSON."""

    def __init__(self, url_csv, url_json, csv_original, csv_salida,
                 json_original, json_salida, manejador_csv, manejador_json):
        self.url_csv = url_csv
        self.url_json = url_json
        self.csv_original = csv_original
        self.csv_salida = csv_salida
        self.json_original = json_original
        self.json_salida = json_salida
        self.manejador_csv = manejador_csv
        self.manejador_json = manejador_json

    def generar(self, ruta_salida="resumen.txt"):
        lineas = [
            "RESUMEN DE MANEJO DE ARCHIVOS CSV, JSON Y TXT",
            "=" * 48,
            f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "1. ORIGEN DE LOS DATOS",
            f"URL de origen CSV: {self.url_csv}",
            f"URL de origen JSON: {self.url_json}",
            "",
            "2. ARCHIVOS PROCESADOS",
            f"CSV original: {self.csv_original}",
            f"CSV modificado guardado en: {self.csv_salida}",
            f"JSON original: {self.json_original}",
            f"JSON modificado guardado en: {self.json_salida}",
            "",
            "3. CLASES Y MÉTODOS UTILIZADOS",
            "ManejadorCSV: importar(), actualizar_valor(), guardar().",
            "ManejadorJSON: importar(), actualizar_valor(), guardar().",
            "GeneradorResumenTXT: generar().",
            "Módulos estándar: csv, json, pathlib, datetime.",
            "",
            "4. MODIFICACIONES REALIZADAS EN CSV",
            *(self.manejador_csv.modificaciones or ["No se registraron modificaciones."]),
            "",
            "5. MODIFICACIONES REALIZADAS EN JSON",
            *(self.manejador_json.modificaciones or ["No se registraron modificaciones."]),
            "",
            "6. CANTIDAD DE REGISTROS PROCESADOS",
            f"Registros CSV: {self.manejador_csv.cantidad_registros}",
            f"Registros JSON: {self.manejador_json.registros_importados}",
            "",
            "Nota: las URL deben corresponder a los archivos descargados manualmente desde Hugging Face.",
            ""
        ]
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        ruta_salida.write_text("\n".join(lineas), encoding="utf-8")
        return str(ruta_salida)
