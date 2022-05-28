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
QUARTERS = ['1t2020', '2t2020', '3t2020', '4t2020',
            '1t2021', '2t2021', '3t2021', '4t2021']

TABLE_RELATORIO = """
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
        """
# Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
FIRST_SCRIPT = """
    SELECT razão_social, vl_saldo_final, vl_saldo_inicial, vl_saldo_final - vl_saldo_inicial AS despesas FROM relatorio, 4t2021
    WHERE reg_ans = registro_ans AND descricao like "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    ORDER BY despesas DESC
    LIMIT 10
    """
# Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
SECOND_SCRIPT = """
    SELECT razão_social, vl_saldo_final AS despesas FROM relatorio, 1t2021 UNION 
    SELECT razão_social, vl_saldo_final AS despesas FROM relatorio, 2t2021 UNION 
    SELECT razão_social, vl_saldo_final AS despesas FROM relatorio, 3t2021 UNION
    SELECT razão_social, vl_saldo_final - vl_saldo_inicial AS despesas FROM relatorio, 4t2021
    WHERE reg_ans = registro_ans AND descricao like "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    ORDER BY despesas DESC
    LIMIT 10
    """


def create_table_relatorio():
    """Ler o css da tabela relatorio_cadop e upar ela na tabela do banco de dados"""
    try:
        engine = create_engine(
            "mysql+mysqldb://root:HYGy8xNh3#a$We@localhost/db_intuitive_care")
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute(TABLE_RELATORIO)

        data = pandas.read_csv('Relatorio_cadop teste 3.csv',
                               encoding='ANSI', sep=';', header=2)
        data_frame = pandas.DataFrame(data)
        data_frame.rename(columns={'Registro ANS': 'Registro_ANS', 'Razão Social': 'Razão_Social', 'Nome Fantasia': 'Nome_Fantasia',
                          'Endereço eletrônico': 'Endereço_eletrônico', 'Cargo Representante': 'Cargo_Representante', 'Data Registro ANS': 'Data_Registro_ANS'}, inplace=True)
        data_frame.to_sql(con=engine, name='relatorio',
                          index=False, if_exists='append')
        cursor.close()
        connection.commit()
    except (Exception) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def create_tables():
    try:
        mydb = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database=DATABASE)
        cursor = mydb.cursor()
        connection = create_engine(
            "mysql+mysqldb://root:HYGy8xNh3#a$We@localhost/db_intuitive_care")
        for quarter in QUARTERS:
            if(quarter != '4t2021'):
                cursor.execute(f"""
                    CREATE TABLE {quarter}(
                        DATA text,
                        REG_ANS bigint,
                        CD_CONTA_CONTABIL bigint,
                        DESCRICAO text,
                        VL_SALDO_FINAL text
                    )
                    """)
                data = pandas.read_csv(
                    quarter + '.csv', encoding='ANSI', sep=';')
                data_frame = pandas.DataFrame(data)
                data_frame.to_sql(con=connection, name=quarter,
                                  index=False, if_exists='append')
            else:
                cursor.execute(f"""
                    CREATE TABLE {quarter}(
                        DATA text,
                        REG_ANS bigint,
                        CD_CONTA_CONTABIL bigint,
                        DESCRICAO text,
                        VL_SALDO_INICIAL text,
                        VL_SALDO_FINAL text
                    )
                    """)
                data = pandas.read_csv(
                    quarter + '.csv', encoding='UTF-8', sep=';')
                data_frame = pandas.DataFrame(data)
                data_frame.to_sql(con=connection, name=quarter,
                                  index=False, if_exists='append')
        cursor.close()
        mydb.commit()
    except (Exception) as error:
        print(error)
    finally:
        if mydb is not None:
            mydb.close()


create_table_relatorio()
#create_tables()
