"""Clase para importar, modificar y guardar archivos JSON con el módulo json."""

import io
import json


class ManejadorJSON:
    """Importa un JSON con json.load, modifica sus registros y guarda un JSON nuevo con json.dump.

    Hugging Face publica muchos archivos .json en formato JSON Lines (un objeto por línea).
    Por eso importar() lee cada línea con json.load; si el archivo es un JSON estándar
    (una lista de objetos), lo lee completo con json.load. El archivo guardado siempre es
    un JSON estándar: una lista de objetos escrita con json.dump.
    """

    def __init__(self, ruta_original):
        self.ruta_original = ruta_original
        self.ruta_guardado = None
        self.registros = []
        self.formato_original = None
        self.registros_importados = 0
        self.modificaciones = []
        self.metodos_usados = []

    def _registrar_metodo(self, nombre):
        if nombre not in self.metodos_usados:
            self.metodos_usados.append(nombre)

    def importar(self):
        """Carga el archivo original y devuelve una lista de diccionarios."""
        with open(self.ruta_original, "r", encoding="utf-8") as archivo:
            primer_caracter = archivo.read(1)
            archivo.seek(0)
            if primer_caracter == "[":
                # JSON estándar: el archivo completo es una lista de objetos.
                self.registros = json.load(archivo)
                self.formato_original = "JSON (lista de objetos)"
            else:
                # JSON Lines: cada línea es un objeto JSON independiente.
                self.registros = [json.load(io.StringIO(linea)) for linea in archivo if linea.strip()]
                self.formato_original = "JSON Lines (un objeto por línea)"
        self.registros_importados = len(self.registros)
        self._registrar_metodo("importar()")
        return self.registros

    def actualizar_valor(self, campo, valor_anterior, valor_nuevo):
        """Reemplaza valor_anterior por valor_nuevo en un campo. Devuelve la cantidad de cambios."""
        cambios = 0
        for registro in self.registros:
            if campo not in registro:
                raise KeyError(f"El campo '{campo}' no existe en el registro {registro.get('id')}.")
            if registro[campo] == valor_anterior:
                registro[campo] = valor_nuevo
                cambios += 1
        self.modificaciones.append(
            f"Actualizar valor: campo '{campo}', '{valor_anterior}' -> '{valor_nuevo}' ({cambios} registros)"
        )
        self._registrar_metodo("actualizar_valor()")
        return cambios

    def agregar_registro(self, registro):
        """Agrega un registro nuevo (diccionario) al final de la lista."""
        self.registros.append(dict(registro))
        self.modificaciones.append(f"Agregar registro: id = '{registro.get('id')}'")
        self._registrar_metodo("agregar_registro()")
        return registro

    def eliminar_registro(self, campo, valor):
        """Elimina los registros cuyo campo sea igual a valor. Devuelve la cantidad eliminada."""
        antes = len(self.registros)
        self.registros = [r for r in self.registros if r.get(campo) != valor]
        eliminados = antes - len(self.registros)
        self.modificaciones.append(f"Eliminar registro: {campo} = '{valor}' ({eliminados} registros)")
        self._registrar_metodo("eliminar_registro()")
        return eliminados

    def guardar(self, ruta_salida):
        """Escribe la lista de registros en un archivo JSON nuevo con json.dump (no toca el original)."""
        if ruta_salida == self.ruta_original:
            raise ValueError("La ruta de salida debe ser distinta del archivo original.")
        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, ensure_ascii=False, indent=2)
        self.ruta_guardado = ruta_salida
        self._registrar_metodo("guardar()")
        return ruta_salida

    def obtener_resultados(self):
        """Devuelve los resultados de la ejecución para la clase que genera el resumen."""
        return {
            "clase": "ManejadorJSON",
            "archivo_importado": self.ruta_original,
            "formato_original": self.formato_original,
            "archivo_guardado": self.ruta_guardado,
            "metodos_usados": list(self.metodos_usados),
            "registros_importados": self.registros_importados,
            "registros_guardados": len(self.registros),
            "modificaciones": list(self.modificaciones),
        }
