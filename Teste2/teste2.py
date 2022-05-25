"""
2.1 - Extrair do pdf do anexo I do teste 1 acima os dados da tabela
Rol de Procedimentos e Eventos em Saúde (todas as páginas);
2.2 - Salvar dados em uma tabela estruturada, em csv;
2.3 - Zipar o csv num arquivo "Teste_{seu_nome}.zip".
2.4 - Bônus: Com a legenda no rodapé substituir os dados
abreviados das colunas OD e AMB para as respectivas descrições.
"""
import pandas
from zipfile import ZipFile
import tabula


PATH = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf'
TABLE = 'Rol de Procedimentos e Eventos em Saúde'


def compress_csv():
    """Compacta todos os arquivos."""
    with ZipFile('Teste_Joao_Pedro_Carvalho.zip', 'w') as zip_obj:
        # Adicionar arquivo ao zip.
        zip_obj.write(TABLE + '.csv')


def extract_csv():
    """Extrair as tabelas csv do pdf(Anexo I)"""
    data_frames = tabula.read_pdf(PATH, pages='all')
    data_frame = pandas.concat(data_frames)
    # Modificar os nomes das colunas
    data_frame = data_frame.rename({"OD": "Seg. Odontológica",
                                    "AMB": "Seg. Ambulatorial"}, axis='columns')
    # Faz a comversão do pdf para csv.
    data_frame.to_csv(TABLE + '.csv', mode='a',
                      encoding='utf-8', index=False, header=True)


def main():
    """Metodo main."""
    extract_csv()
    compress_csv()


if __name__ == "__main__":
    main()
