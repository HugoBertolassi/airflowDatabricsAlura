

# montagem do ambiente
## configurando o python e venv na wsl

sudo apt-get update
sudo apt-get upgrade -y
python3 --version

### instalar as bibliotecas pip e venv do Python:
sudo apt install python3-pip -y
sudo apt install python3-venv -y

### Criando um ambiente virtual
mkdir airflow-databricks
cd airflow-databricks
sudo apt install python3-virtualenv
virtualenv curso_datAir

ativação do veenv executamos o seguinte código:
source curso_datAir/bin/activate

code .

## instalando airflow
https://airflow.apache.org/docs/apache-airflow/stable/start.html

PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
export AIRFLOW_HOME=~/airflow
export AIRFLOW_VERSION=3.0.3
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

instalando: pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

Run Airflow Standalone:
airflow standalone

para abrir o airfloe
localhost:8080

foi criada uma pasta "airflow" dentro da pasta padrão do wsl. Dentro delas que vamos salvar as dags e para isso vamos criar uma pasta dags
mkdir /home/bruno/airflow/dags


### instalando extensão airflow-databricks
pip install apache-airflow-providers-databricks

para o erro do setuptools validar a versão do python 3.10, dei downgrade na versão para funcionar a instalação 65.0.0

# configurandp a azure

###alerta de custo
"Gerenciamento de custo". > "Orçamentos" >adicionar, colocar conta, periodo mensal valor 2$

criar conexão databricks databricks
-olhar pára pegar o tier mais barato  
iniciar workspace


# api com os dados

exchange api rates
https://apilayer.com/marketplace/exchangerates_data-api

apikey: JxSTDnwHcbXtWh67iqZjlcLBQUhlC7Wc

aposs criar o etl.
criar um job vinculando o arquivo da extração. 
Pra vincular o job no airflow precisa copiar o id do job criado

# configurando o airflow cm o job do databricks
https://docs.databricks.com/aws/en/jobs/how-to/use-airflow-with-jobs

iniciar o venv e airflow:
cd airflow-databricks
source airflow-databricks/curso_datAir/bin/activate
airflow standalone


abre o airflow no localHost:8080

abre o airflow dentro da base onde criamos a pasta dag
e abrir o vscode com code . 

criar arquivo extraindo-taxas.py (cod no arquivo)

## criando conexao entre databbricks e airflow
https://learn.microsoft.com/en-us/fabric/data-factory/apache-airflow-jobs-run-databricks-job

admin> connections : databricks_default

connection_id: nome da conexão (pode ser qualquer mas coloquei databriks_default)
connectiontype: databricks
host = url da azure com o nome da conexão no databricks
login => deixar vazio para que qualquer usuario logue
password: gerar um access token no site do databricks em usuario>definicoes> programador>tokenAcesso

para testar conexão com o Databricks, é preciso definir o parâmetro test_connection = Enabled dentro do arquivo ~/airflow/airflow.cfg, antes de iniciar a instância standalone. Caso contrário, o botão de testes fica desabilitado.

### erro ao criar dag
ver versão do executor do python, garantir que seja o venv. No canto de baixo do vscoce

erro de importação, instalar modulos faltantes
apache-airflow-providers-fab==1.5.2



# adicionar no job as bbliotecas externas
se for serverless , somente consegumos instalar no notebook

projeto final do curso: https://github.com/alura-cursos/curso-airflow-databricks/tree/main



# vincular github
criar access token classic da conta do github

no databricks em definições>utilizador> contas vinculadas > git integation > selecionar forncedor gi:github

## vincular ao databricks no github
pesquisar por repos dentor do espaço de tranbalho
selecionar criar conexão, github, e colocar access token, projeto github que deseja vincular

Como vinculo dando certo vai aparecer um simbolo de branch dentro da pasta do projeto

dentro da pasta vai aparecer o simbolo da branch e arquivos. Clicando no simbolo da branch vai habilitar para fazer o merge