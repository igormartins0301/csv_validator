# %%
import sys
from pathlib import Path

import pandas as pd
import pandera as pa

sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.models.sales_pandera_val import sales_schema


class CSVFile:
    def __init__(self, file):
        self.file = file
        self.data = self._load_csv()
        self.removed_rows_indices = []

    def _load_csv(self):
        """Carrega o CSV para um DataFrame pandas."""
        return pd.read_csv(self.file)

    def remove_null_rows(self):
        """Remove linhas com valores nulos e retorna os índices
        dessas linhas."""
        null_rows = self.data[self.data.isnull().any(axis=1)]
        self.removed_rows_indices = null_rows.index.tolist()
        self.data = self.data.dropna()
        return self.removed_rows_indices

    def validate(self):
        """Valida o DataFrame completo com Pandera."""
        self.data['sale_date'] = pd.to_datetime(
            self.data['sale_date'], errors='coerce'
        )
        try:
            sales_schema.validate(self.data)
        except pa.errors.SchemaError as e:
            raise ValueError(f'Erro na validação Pandera: {e}')

    def process_file(self):
        """Processa o arquivo, remove linhas nulas e valida os dados."""
        self.remove_null_rows()
        self.validate()
        return self.removed_rows_indices
