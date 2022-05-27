# desafios-intuitive-care-backend
Resolução de desafios propostos.

# Test 01 - Web Scraping
- 1.1 Acessar o site: https://www.gov.br/ans/pt-br/assuntos/consumidor/
o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude
- 1.2 Baixar os Anexos I ao Anexo IV
- 1.3 Agrupar os anexos em um mesmo arquivo compactado ZIP.

# Test 02 - Data Extraction
- 2.1 Extrair do pdf do anexo I do teste 1 acima os dados da tabela
Rol de Procedimentos e Eventos em Saúde (todas as páginas).
- 2.2 Salvar dados em uma tabela estruturada, em csv.
- 2.3 Zipar o csv num arquivo "Teste_{seu_nome}.zip".
- 2.4 Bônus: Com a legenda no rodapé substituir os dados
abreviados das colunas OD e AMB para as respectivas descrições.

# Test 03 - Database
- 3.1 Tarefas de Preparação (podem ser feitas manualmente):
```
Baixar os arquivos dos últimos 2 anos no repositório público: http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

Baixar csv anexo: Relatorio_cadop(1) (esta em anexo no e-mail)
```

- 3.2 Criar queries para criar tabelas com as colunas necessárias para o arquivo csv.
- 3.3 Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação,
atenção ao encoding dos arquivos no momento da importação!
- 3.4 Montar uma query analítica que traga a resposta para as seguintes perguntas:
```
Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
```

# Test 04 - API

- 4.1 Tarefas de Preparação (podem ser feitas manualmente):
```
Baixar o CSV que esta em anexo no email.
```
- 4.2 Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de preparação) e retorne as linhas que mais se assemelham.

- 4.3 Criar coleção no Postman para exibir resultado.


# Bibliotecas necessárias para a execução:

```
sudo pip install requests
sudo pip install beautifulsoup4
sudo pip install tabula-py
```


