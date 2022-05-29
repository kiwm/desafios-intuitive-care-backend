"""Ler os arquivos css e coloca no banco de dados"""
import pandas
from sqlalchemy import create_engine
import sqlalchemy

HOST = 'localhost'
USER_NAME = 'root'
PASSWORD = 'HYGy8xNh3#a$We'
DATABASE = 'appdb_intuitive_care'

def create_table():
    """Ler os arquivos css e coloca no banco de dados"""
    try:
        engine = create_engine(
            f"mysql+mysqldb://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE}")
        connection = engine.raw_connection()
        cursor = connection.cursor()
        data = pandas.read_csv(
            'Relatorio_cadop teste 4.csv', encoding='ANSI', sep=';', header=2)
        data_frame = pandas.DataFrame(data)
        # Limpar os dados
        data_frame.rename(columns={'Registro ANS': 'Registro_ANS', 'Razão Social': 'Razão_Social',
                                   'Nome Fantasia': 'Nome_Fantasia',
                                   'Endereço eletrônico': 'Endereço_eletrônico',
                                   'Cargo Representante': 'Cargo_Representante',
                                   'Data Registro ANS': 'Data_Registro_ANS'}, inplace=True)
        data_frame.to_sql(con=engine, name='report',
                          index=False, if_exists='append',
                          chunksize=1000, dtype={'DDD': sqlalchemy.FLOAT, 'Fax': sqlalchemy.FLOAT})
        
        #cursor.execute('ALTER TABLE relatorio ADD PRIMARY KEY (Registro_ANS);')


        cursor.close()
        connection.commit()
    except (Exception) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


create_table()