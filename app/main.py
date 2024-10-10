# app/main.py
import os

import streamlit as st
from storage.blob_storage import BlobStorage
from upload.csv_file import CSVFile


def main():
    st.title('Upload de Arquivos')
    uploaded_file = st.file_uploader('Escolha um arquivo CSV', type='csv')

    if uploaded_file is not None:
        file_path = f'/tmp/{uploaded_file.name}'
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        csv_file = CSVFile(file=file_path)
        try:
            removed_index = csv_file.process_file()
            if removed_index:
                st.warning(
                    f"""linhas removidas devido a valores nulos:{removed_index}
                    Faça a correção dessas linhas e envie um novo arquivo."""
                )
            blob_storage = BlobStorage()
            blob_storage.upload(
                filename=uploaded_file.name,
                file_path=file_path,
                container_name='csv',
            )
            st.success('Arquivo validado com sucesso!')
        except ValueError as e:
            st.error(f'Erro: {str(e)}')

        os.remove(file_path)


if __name__ == '__main__':
    main()
