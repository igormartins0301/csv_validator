# %%
import os

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()


class BlobStorage:
    def __init__(self):
        self.connection_string = self._get_secret_from_key_vault()
        self.connection = self.connect()

    @staticmethod
    def _get_secret_from_key_vault():
        """Recupera o segredo do Azure Key Vault."""
        client_id = os.environ.get('AZURE_CLIENT_ID')
        tenant_id = os.environ.get('AZURE_TENANT_ID')
        client_secret = os.environ.get('AZURE_CLIENT_SECRET')
        vault_url = os.environ.get('AZURE_VAULT_URL')
        secret_name = os.environ.get('AZURE_SECRET_NAME')

        credentials = ClientSecretCredential(
            client_id=client_id,
            client_secret=client_secret,
            tenant_id=tenant_id,
        )

        secret_client = SecretClient(
            vault_url=vault_url, credential=credentials
        )
        secret = secret_client.get_secret(secret_name)
        return secret.value

    def connect(self):
        """Estabelece a conexão com o Blob Storage usando a connection string."""
        try:
            blob_service_client = BlobServiceClient.from_connection_string(
                self.connection_string
            )
            print('Conexão estabelecida com sucesso!')
            return blob_service_client
        except Exception as e:
            print(f'Erro ao conectar ao Blob Storage: {str(e)}')
            return None

    def upload(self, file_path, container_name, blob_name):
        """Realiza o upload de um arquivo para o Blob Storage."""
        try:
            blob_client = self.connection.get_blob_client(
                container=container_name, blob=blob_name
            )
            with open(file_path, 'rb') as data:
                blob_client.upload_blob(data, overwrite=True)
            print('Arquivo enviado com sucesso!')
        except Exception as e:
            print(f'Erro ao fazer upload do arquivo: {str(e)}')
