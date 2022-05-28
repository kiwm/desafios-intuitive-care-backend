def table_report():
    """Sql para criar a tabela do relatorio"""
    return """
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

def table_quarter(quarter):
    return f"""
    CREATE TABLE trimestre_{quarter}(
    DATA text,
    REG_ANS bigint,
    CD_CONTA_CONTABIL bigint,
    DESCRICAO text,
    VL_SALDO_FINAL float
    )
    """

def table_last_quarter(quarter):
    return f"""
    CREATE TABLE trimestre_{quarter}(
    DATA text,
    REG_ANS bigint,
    CD_CONTA_CONTABIL bigint,
    DESCRICAO text,
    VL_SALDO_INICIAL float,
    VL_SALDO_FINAL float
    )
    """

def first_script():
    """Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?"""
    return """
    SELECT razão_social, vl_saldo_final, vl_saldo_inicial, vl_saldo_final - vl_saldo_inicial AS despesas FROM relatorio, trimestre_4t2021
    WHERE reg_ans = registro_ans AND descricao LIKE "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    ORDER BY despesas DESC
    LIMIT 10
    """


def second_script():
    """Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?"""
    return """
    SELECT razão_social, vl_saldo_final AS despesas FROM relatorio, trimestre_1t2021 
    WHERE reg_ans = registro_ans AND descricao 
    LIKE "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "     
    UNION
    SELECT razão_social, vl_saldo_final AS despesas FROM relatorio, trimestre_2t2021 
    WHERE reg_ans = registro_ans AND descricao 
    LIKE "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    UNION
    SELECT razão_social, vl_saldo_final AS despesas FROM relatorio, trimestre_3t2021 
    WHERE reg_ans = registro_ans AND descricao 
    LIKE "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
    UNION
    SELECT razão_social, vl_saldo_final - vl_saldo_inicial AS despesas FROM relatorio, trimestre_4t2021 
    WHERE reg_ans = registro_ans AND descricao 
    LIKE "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "     
    ORDER BY despesas DESC  LIMIT 10
    """
