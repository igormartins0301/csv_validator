from abc import ABC, abstractmethod


class AbstractFile(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def validate(self):
        """Valida a estrutura e os tipos de dados do arquivo."""
        pass

    @abstractmethod
    def upload_to_storage(self):
        """Faz o upload do arquivo para o Blob Storage."""
        pass
