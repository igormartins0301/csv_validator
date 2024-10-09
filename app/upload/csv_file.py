# app/upload/csv_file.py
import pandas as pd

from app.models.csv_model import CSVSchemaModel
from app.storage.blob_storage import BlobStorage

from .abstract_file import AbstractFile


class CSVFile(AbstractFile):
    def validate(self):
        """Valida o CSV usando Pydantic e Pandera."""
        try:
            df = pd.read_csv(self.file_path)
            CSVSchemaModel.validate(df)
        except Exception as e:
            raise ValueError(f'Erro de validação do CSV: {str(e)}')

    def upload_to_storage(self):
        """Faz o upload do CSV para o Blob Storage."""
        storage = BlobStorage()
        storage.upload(self.file_path, 'csv-folder/')
