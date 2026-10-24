# Actividad S10 – Carga y creación de dataset

## Contenido
- `dataset_loader.py`: clase que carga un dataset de Hugging Face y lo convierte en DataFrame.
- `dataset_summarizer.py`: clase que resume un DataFrame y guarda el informe en TXT.
- `actividad_s10.ipynb`: notebook que coordina las clases y realiza cuatro transformaciones.
- `requirements.txt`: dependencias.

## Requisitos
Python 3.10 o superior recomendado.

Instala las dependencias ejecutando en una terminal:
```bash
pip install -r requirements.txt
```

## Ejecución
1. Descomprime la carpeta y abre `actividad_s10.ipynb` en Jupyter.
2. Asegúrate de que los dos archivos `.py` estén en la misma carpeta que el notebook.
3. Ejecuta las celdas en orden.
4. La primera ejecución puede requerir conexión a Internet para descargar el dataset de Hugging Face.
5. El notebook genera `resumen_dataset.txt` con el resumen del DataFrame transformado.

## Dataset
Se utiliza `scikit-learn/iris`, como ejemplo sugerido en las instrucciones de la actividad. Si Hugging Face cambia la disponibilidad o la configuración del dataset, revisa la ficha del conjunto de datos y ajusta `dataset_id` o `split`.

## Transformaciones incluidas
1. Renombrar la primera columna.
2. Seleccionar las columnas disponibles (se conservan todas las columnas del dataset en una nueva tabla de trabajo).
3. Tratar los valores nulos de columnas numéricas con la mediana.
4. Filtrar filas que tengan un valor presente en la primera columna.

El notebook muestra los resultados de cada transformación y genera el resumen después de aplicarlas.

## GitHub
Publica los archivos en un repositorio y registra avances mediante commits descriptivos. Antes de entregar, verifica que el notebook se ejecute de principio a fin y que el TXT generado esté incluido en el repositorio.