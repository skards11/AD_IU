
import csv
from pathlib import Path


class ManejadorCSV:
    """Importa, modifica y guarda datos en archivos CSV."""

    def __init__(self, ruta_archivo):
        self.ruta_archivo = Path(ruta_archivo)
        self.encabezados = []
        self.registros = []
        self.modificaciones = []
    @property
    def cantidad_registros(self):
        return len(self.registros)

    def importar(self):
        """Lee los encabezados y registros del archivo CSV."""
        with self.ruta_archivo.open(
            "r", encoding="utf-8-sig", newline=""
        ) as archivo:
            lector = csv.DictReader(archivo)
            self.encabezados = lector.fieldnames or []
            self.registros = list(lector)

        return self.encabezados, self.registros

    def actualizar_valor(self, columna, valor_anterior, valor_nuevo):
        """Actualiza los valores coincidentes en una columna."""
        if not self.registros:
            self.importar()

        if columna not in self.encabezados:
            raise KeyError(f"La columna '{columna}' no existe.")

        cambios = 0

        for registro in self.registros:
            if registro.get(columna) == valor_anterior:
                registro[columna] = valor_nuevo
                cambios += 1

        self.modificaciones.append(
            f"Columna '{columna}': '{valor_anterior}' -> "
            f"'{valor_nuevo}' ({cambios} cambios)"
        )

        return cambios

    def guardar(self, ruta_salida):
        """Guarda los registros en un archivo CSV nuevo."""
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        with ruta_salida.open(
            "w", encoding="utf-8-sig", newline=""
        ) as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=self.encabezados
            )
            escritor.writeheader()
            escritor.writerows(self.registros)

        return ruta_salida
