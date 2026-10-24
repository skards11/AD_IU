from datasets import load_dataset


class HFDatasetLoader:
    """Carga un dataset de Hugging Face y lo convierte en un DataFrame de pandas."""

    def __init__(self, dataset_id: str, split: str = "train"):
        self.dataset_id = dataset_id
        self.split = split

    def load_data(self):
        """Carga la partición solicitada y devuelve un DataFrame."""
        dataset = load_dataset(self.dataset_id, split=self.split)
        return dataset.to_pandas()