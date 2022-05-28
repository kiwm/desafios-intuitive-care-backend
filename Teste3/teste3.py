"""
- 3.2 Criar queries para criar tabelas com as colunas necessárias para o arquivo csv.
- 3.3 Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos
nas tarefas de preparação, atenção ao encoding dos arquivos no momento da importação!
- 3.4 Montar uma query analítica que traga a resposta para as seguintes perguntas:
Quais as 10 operadoras que mais tiveram despesas com
"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
no último trimestre?
Quais as 10 operadoras que mais tiveram despesas com
"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
no último ano?
"""

from sqlalchemy import create_engine
import pandas
import sqlalchemy
from queries import table_report, table_quarter, table_last_quarter, first_script, second_script


HOST = 'localhost'
USER_NAME = 'root'
PASSWORD = 'HYGy8xNh3#a$We'
DATABASE = 'db_intuitive_care'
QUARTERS = ['1t2020', '2t2020', '3t2020', '4t2020',
            '1t2021', '2t2021', '3t2021', '4t2021']


def create_table_report():
    """Ler o css da tabela relatorio_cadop e coloca no banco de dados"""
    try:
        engine = create_engine(
            f"mysql+mysqldb://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE}")
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute(table_report())
        data = pandas.read_csv('Relatorio_cadop teste 3.csv',
                               encoding='ANSI', sep=';', header=2)
        data_frame = pandas.DataFrame(data)
        # Limpar os dados
        data_frame.rename(columns={'Registro ANS': 'Registro_ANS', 'Razão Social': 'Razão_Social',
                                   'Nome Fantasia': 'Nome_Fantasia',
                                   'Endereço eletrônico': 'Endereço_eletrônico',
                                   'Cargo Representante': 'Cargo_Representante',
                                   'Data Registro ANS': 'Data_Registro_ANS'}, inplace=True)
        data_frame.to_sql(con=engine, name='relatorio',
                          index=False, if_exists='append', chunksize=1000)
        cursor.close()
        connection.commit()
    except (Exception) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def create_tables():
    """Ler os arquivos css e coloca no banco de dados"""
    try:
        engine = create_engine(
            f"mysql+mysqldb://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE}")
        connection = engine.raw_connection()
        cursor = connection.cursor()
        for quarter in QUARTERS:
            # Pular a última tabela pois ela tem uma coluna a mais.
            if quarter != '4t2021':
                cursor.execute(table_quarter(quarter))
                data = pandas.read_csv(
                    quarter + '.csv', encoding='ANSI', sep=';', engine='c')
                data_frame = pandas.DataFrame(data)
                # Limpar os dados
                data_frame.replace(',', '.', regex=True, inplace=True)
                data_frame.to_sql(con=engine, name='trimestre_'+quarter,
                                  index=False, if_exists='append',
                                  chunksize=1000, dtype={'VL_SALDO_FINAL': sqlalchemy.FLOAT})
            else:
                cursor.execute(table_last_quarter(quarter))
                data = pandas.read_csv(
                    quarter + '.csv', encoding='UTF-8', sep=';')
                data_frame = pandas.DataFrame(data)
                # Limpar os dados
                data_frame.replace(',', '.', regex=True, inplace=True)
                data_frame.to_sql(con=engine, name='trimestre_'+quarter,
                                  index=False, if_exists='append', chunksize=1000,
                                  dtype={'VL_SALDO_FINAL': sqlalchemy.FLOAT,
                                         'VL_SALDO_INICIAL': sqlalchemy.FLOAT})
        cursor.close()
        connection.commit()
    except (Exception) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def show_select(querie):
    """executa uma consulta e mostra o resultado dela no console"""
    try:
        engine = create_engine(
            f"mysql+mysqldb://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE}")
        connection = engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute(querie)
        # Mostar o resultado da consulta
        records = cursor.fetchone()
        while records is not None:
            print(records)
            records = cursor.fetchone()
        cursor.close()
        connection.commit()
    except (Exception) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def main():
    """Metodo main."""
    create_table_report()
    create_tables()
    show_select(first_script())
    show_select(second_script())


if __name__ == "__main__":
    main()
