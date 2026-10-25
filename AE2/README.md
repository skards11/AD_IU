# AE2 – Manejo de archivos CSV, JSON y TXT

Analítica de Datos – IU Digital de Antioquia
Daniela Cataño Hernández · John Freddy Ocampo Ochoa · Óscar Alonso De La Pava Suárez

## Contenido

| Archivo | Descripción |
|---|---|
| `manejador_csv.py` | Clase `ManejadorCSV`: importa con `csv.reader`, modifica (`actualizar_valor`, `agregar_registro`, `eliminar_registro`) y guarda con `csv.writer`, incluyendo encabezados. |
| `manejador_json.py` | Clase `ManejadorJSON`: importa con `json.load`, modifica (mismos métodos) y guarda con `json.dump`. |
| `generador_resumen_txt.py` | Clase `GeneradorResumenTXT`: recibe las URL de origen y los resultados de las otras dos clases y escribe `resumen.txt`. |
| `actividad_ae2.ipynb` | Notebook ejecutado que coordina las tres clases. |
| `datos/originales/` | Archivos descargados manualmente de Hugging Face, sin cambios. |
| `datos/modificados/` | Archivos nuevos generados por las clases. |
| `resumen.txt` | Resumen generado al ejecutar el notebook. |

## Origen de los datos

| Formato | Archivo | URL |
|---|---|---|
| CSV | `datos/originales/Iris.csv` | https://huggingface.co/datasets/scikit-learn/iris/blob/main/Iris.csv |
| JSON | `datos/originales/train.json` | https://huggingface.co/datasets/PhdDz/Paper_1_BioASQ-dataset/blob/main/train.json |

`train.json` está en formato JSON Lines (un objeto por línea). `ManejadorJSON` lee cada línea con `json.load` y guarda el resultado como un JSON estándar (lista de objetos) con `json.dump`.

## Modificaciones

| Formato | Método | Cambio | Registros |
|---|---|---|---|
| CSV | `actualizar_valor()` | `Species`: `Iris-setosa` → `setosa` | 50 |
| CSV | `agregar_registro()` | Nueva flor con `Id` 151 | 150 → 151 |
| JSON | `actualizar_valor()` | `label`: `yes` → `sí` | 769 |
| JSON | `eliminar_registro()` | Se elimina `id` = `converted_4560` | 1017 → 1016 |

## Pasos antes de ejecución

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  
   pip install -r requirements.txt
   ```
(Apoyo para creación del codigo con Claude Code)

