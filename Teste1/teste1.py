"""
1.1 - Acessar o site: https://www.gov.br/ans/pt-br/assuntos/consumidor/
o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude
1.2 - Baixar os Anexos I ao Anexo IV
1.3 - Agrupar os anexos em um mesmo arquivo compactado ZIP.
"""

from zipfile import ZipFile
from os.path import basename
import os
from bs4 import BeautifulSoup
import requests

URL = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
FILENAMELIST = ['Anexo I - Lista completa de procedimentos (.pdf)',
                'Anexo I - Lista completa de procedimentos (.xlsx)',
                'Anexo II - Diretrizes de utilização (.pdf)',
                'Anexo III - Diretrizes clínicas (.pdf)',
                'Anexo IV - Protocolo de utilização (.pdf)']


def get_soup(url):
    """Retorna um objeto beautifulsoup."""
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


def download_file(url, file_name):
    """Faz o download dos arquivos."""
    try:
        # Stream = true prepara os dados para serem lidos em chunks.
        with requests.get(url, stream=True) as request:
            with open('arquivosTeste1/' + file_name, 'wb') as file:
                # Limita o uso de memória independente do tamanho do arquivo baixado.
                for chunk in request.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
    except Exception as exeption:
        print(exeption)


def compress_files():
    """Compacta todos os arquivos."""
    try:
        with ZipFile('arquivosTeste1.zip', 'w') as zip_obj:
            directory = os.getcwd() + '/arquivosTeste1'
            # Interar todos os arquivos no diretório.
            for folder_name, sub_folders, file_names in os.walk(directory):
                for file_name in file_names:
                    # Criar o caminho completo do arquivo no diretório.
                    file_path = os.path.join(folder_name, file_name)
                    # Adicionar arquivo ao zip.
                    zip_obj.write(file_path, basename(file_path))
    except Exception as exeption:
        print(exeption)


def download_attachments():
    """Encontra os links buscando pelo texto"""
    soup = get_soup(URL)
    for name in FILENAMELIST:
        # Encontra e atribui o link com o texto correspondente.
        link = soup.find(["a"], text=name)
        # Atribui apenas o conteudo do atributo href(url)
        url_to_download = link['href']
        file_name = url_to_download.split('/')[-1]
        download_file(url_to_download, file_name)


def main():
    """Metodo main."""
    download_attachments()
    compress_files()


if __name__ == "__main__":
    main()
