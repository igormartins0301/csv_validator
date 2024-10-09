# app/main.py
import streamlit as st

from app.upload.csv_file import CSVFile


def main():
    st.title('Upload de Arquivos')
    file = st.file_uploader('Escolha um arquivo CSV', type=['csv'])

    if file:
        csv_file = CSVFile(file)
        try:
            csv_file.validate()
            csv_file.upload_to_storage()
            st.success('Arquivo validado e enviado com sucesso!')
        except ValueError as e:
            st.error(f'Erro: {str(e)}')


if __name__ == '__main__':
    main()
