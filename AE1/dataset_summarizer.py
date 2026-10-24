class DatasetSummarizer:
    """Genera un resumen descriptivo de un DataFrame en un archivo de texto."""

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def generate_summary(self, output_path="resumen_dataset.txt"):
        """Escribe dimensiones, columnas, tipos, nulos y estadísticas descriptivas."""
        df = self.dataframe

        with open(output_path, "w", encoding="utf-8") as file:
            file.write("RESUMEN DEL DATASET TRANSFORMADO\\n")
            file.write("=" * 36 + "\\n\\n")
            file.write(f"Cantidad de filas: {df.shape[0]}\\n")
            file.write(f"Cantidad de columnas: {df.shape[1]}\\n\\n")

            file.write("NOMBRES DE LAS COLUMNAS\\n")
            file.write("-" * 24 + "\\n")
            file.write(", ".join(map(str, df.columns)) + "\\n\\n")

            file.write("TIPOS DE DATOS\\n")
            file.write("-" * 15 + "\\n")
            file.write(df.dtypes.astype(str).to_string() + "\\n\\n")

            file.write("VALORES NULOS POR COLUMNA\\n")
            file.write("-" * 25 + "\\n")
            file.write(df.isna().sum().to_string() + "\\n\\n")

            file.write("ESTADISTICAS DESCRIPTIVAS\\n")
            file.write("-" * 25 + "\\n")
            file.write(df.describe(include="all").transpose().to_string())

        return output_path
