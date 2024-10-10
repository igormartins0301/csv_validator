# %%
import os

from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()


class BlobStorage:
    def __init__(self):
        self.credentials = self._get_credentials()
        self.account_url = os.environ.get('AZURE_STORAGE_URL')
        self.connection = self.connect()

    @staticmethod
    def _get_credentials():
        """Recupera o segredo do Azure Key Vault."""
        client_id = os.environ.get('AZURE_CLIENT_ID')
        tenant_id = os.environ.get('AZURE_TENANT_ID')
        client_secret = os.environ.get('AZURE_CLIENT_SECRET')

        credentials = ClientSecretCredential(
            client_id=client_id,
            client_secret=client_secret,
            tenant_id=tenant_id,
        )
        return credentials

    def connect(self):
        """Estabelece a conexão com o Blob Storage usando as credenciais."""
        try:
            blob_service_client = BlobServiceClient(
                account_url=self.account_url, credential=self.credentials
            )
            print('Conexão estabelecida com sucesso!')
            return blob_service_client
        except Exception as e:
            print(f'Erro ao conectar ao Blob Storage: {str(e)}')
            return None

    def upload(self, filename, file_path, container_name):
        """Realiza o upload de um arquivo para o Blob Storage."""
        try:
            container_client = self.connection.get_container_client(
                container=container_name
            )
            with open(file_path, 'rb') as data:
                container_client.upload_blob(
                    name=filename, data=data, overwrite=True
                )
            print('Arquivo enviado com sucesso!')
        except Exception as e:
            print(f'Erro ao fazer upload do arquivo: {str(e)}')
