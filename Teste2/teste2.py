"""
2.1 - Extrair do pdf do anexo I do teste 1 acima os dados da tabela
Rol de Procedimentos e Eventos em Saúde (todas as páginas);
2.2 - Salvar dados em uma tabela estruturada, em csv;
2.3 - Zipar o csv num arquivo "Teste_{seu_nome}.zip".
2.4 - Bônus: Com a legenda no rodapé substituir os dados
abreviados das colunas OD e AMB para as respectivas descrições.
"""


from zipfile import ZipFile
import tabula


PATH = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf'
TABLE_NAME = 'Rol de Procedimentos e Eventos em Saúde.csv'


def compress_csv():
    """Compacta todos os arquivos."""
    with ZipFile('Teste2/Rol de Procedimentos e Eventos em Saúde.zip', 'w') as zip_obj:
        # Adicionar arquivo ao zip.
        zip_obj.write('Teste2/'+TABLE_NAME)


def extract_csv():
    """Extrair os dataframes do pdf(Anexo I)."""
    data_frames = tabula.read_pdf(PATH, pages='all')

    for data_frame in data_frames:
        # Modificar os nomes das colunas.
        data_frame = data_frame.rename({"OD": "Seg. Odontológica",
                                        "AMB": "Seg. Ambulatorial",
                                        "RN\r(alteração)": "RN (alteração)"}, axis='columns')
        # Faz uma limpeza nos dados.
        data_frame = data_frame.replace(',', '.', regex=True)
        data_frame = data_frame.replace('\r',  ' ', regex=True)
        # Faz a comversão do pdf para csv, mode = append.
        data_frame.to_csv('Teste2/'+TABLE_NAME,
                          encoding='utf-8', index=False, mode='a')


def main():
    """Metodo main."""
    extract_csv()
    compress_csv()


if __name__ == "__main__":
    main()
