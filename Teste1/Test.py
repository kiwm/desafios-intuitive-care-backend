
from zipfile import ZipFile
from bs4 import BeautifulSoup
from os.path import basename
import requests, os

URL = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
FILENAMELIST = ['Anexo I - Lista completa de procedimentos (.pdf)', 'Anexo I - Lista completa de procedimentos (.xlsx)', 'Anexo II - Diretrizes de utilização (.pdf)', 'Anexo III - Diretrizes clínicas (.pdf)', 'Anexo IV - Protocolo de utilização (.pdf)']

def getSoup(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser') #Retorna um objeto beautifulsoup.

def downloadFile(url, fileName):
    try:
        with requests.get(url, stream = True) as request: #Stream = true prepara os dados para serem lidos em chunks.
            with open('arquivosTeste1/' + fileName, 'wb') as file: 
                for chunk in request.iter_content(chunk_size=8192): #Limita o uso de memória independente do tamanho do arquivo baixado.
                    if chunk:
                        file.write(chunk) 
    except Exception as e:
        print(e)

def compressFiles():
    try:
        with ZipFile('arquivosTeste1.zip', 'w') as zipObj:
            directory = os.getcwd() + '/arquivosTeste1'
            for folderName, subfolders, filenames in os.walk(directory): #Interar todos os arquivos no diretório.
                for filename in filenames:
                    filePath = os.path.join(folderName, filename) #Criar o caminho completo do arquivo no diretório.
                    zipObj.write(filePath, basename(filePath)) #Adicionar arquivo ao zip.
    except Exception as e:
        print(e)

def downloadAttachments():
    soup = getSoup(URL)
    for name in FILENAMELIST:
        link = soup.find(["a"], text = name) #Encontra é atribui o link com o texto correspondente. 
        urlToDownload = link['href'] #Atribui apenas o conteudo do atributo href(url) 
        fileName = urlToDownload.split('/')[-1]
        downloadFile(urlToDownload, fileName)

downloadAttachments()
compressFiles()  