from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime

with DAG(
  'Executando-notebook-etl',
  start_date=datetime(2025, 7, 24), # Lembre de colocar para sua data, para não ultrapassar as 250 requisições
  schedule="0 9 * * *",  # Todos os dias as 9 da manhã
  ) as dag_executando_notebook_extracao:
    
    extraindo_dados = DatabricksRunNowOperator(
    task_id = 'Extraindo-conversoes',
    databricks_conn_id = 'databricks_default',
    job_id = 893209726493369,
    notebook_params={"data_execucao": '{{data_interval_end.strftime("%Y-%m-%d")}}'}
  )
    transformando_dados = DatabricksRunNowOperator(
        task_id = 'transformando-dados',
        databricks_conn_id = 'databricks_default',
        job_id = 1080437218722516
    )

    enviando_relatorio = DatabricksRunNowOperator(
    task_id = 'enviando-relatorio',
    databricks_conn_id = 'databricks_default',
    job_id = "462078593554248"
  )
    
    extraindo_dados >> transformando_dados >> enviando_relatorio
# Este DAG executa um notebook de ETL no Databricks, extraindo dados, transformando-os e enviando um relatório.
# Certifique-se de que os IDs dos trabalhos (job_id) estejam corretos e correspondam aos seus notebooks no Databricks.
# O parâmetro 'data_execucao' é passado para o notebook de extração, permitindo que ele saiba a data de execução do DAG.