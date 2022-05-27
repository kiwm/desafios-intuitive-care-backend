"""
- 3.2 Criar queries para criar tabelas com as colunas necessárias para o arquivo csv.
- 3.3 Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação,
atenção ao encoding dos arquivos no momento da importação!
- 3.4 Montar uma query analítica que traga a resposta para as seguintes perguntas:
Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
"""

from sqlalchemy import create_engine
import mysql.connector
import pandas


HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'HYGy8xNh3#a$We'
DATABASE = 'db_intuitive_care'

TABLE_RELATORIO = ("""
            CREATE TABLE relatorio(
            Registro_ANS bigint,
            CNPJ text,
            Razão_Social text,
            Nome_Fantasia text,
            Modalidade text,
            Logradouro text,
            Número text,
            Complemento text,
            Bairro text,
            Cidade text,
            UF text,
            CEP bigint,
            DDD double,
            Telefone text,
            Fax double,
            Endereço_eletrônico text,
            Representante text,
            Cargo_Representante text,
            Data_Registro_ANS text
        )
        """)


def create_table_relatorio():
    try:
        mydb = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database=DATABASE)
        cursor = mydb.cursor()
        cursor.execute(TABLE_RELATORIO)
        connection = create_engine(
            "mysql+mysqldb://root:HYGy8xNh3#a$We@localhost/db_intuitive_care")
        data = pandas.read_csv('Relatorio_cadop teste 3.csv',
                               encoding='ANSI', sep=';', header=2)
        data_frame = pandas.DataFrame(data)
        data_frame.rename(columns={'Registro ANS': 'Registro_ANS', 'Razão Social': 'Razão_Social', 'Nome Fantasia': 'Nome_Fantasia',
                          'Endereço eletrônico': 'Endereço_eletrônico', 'Cargo Representante': 'Cargo_Representante', 'Data Registro ANS': 'Data_Registro_ANS'}, inplace=True)
        data_frame.to_sql(con=connection, name='relatorio',
                          index=False, if_exists='append')
        cursor.close()
        mydb.commit()
    except (Exception) as error:
        print(error)
    finally:
        if mydb is not None:
            mydb.close()


create_table_relatorio(TABLE_RELATORIO)
