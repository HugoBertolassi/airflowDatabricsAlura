# airflowDatabricsAlura

# premissa do projeto

O que aprenderemos?
Vamos imaginar o seguinte cenário: trabalhamos em uma empresa que importa produtos de diferentes países.

Para ter melhor previsão dos gastos, é necessário acompanhar as flutuações de diferentes moedas.

Além disso, devido à natureza remota do trabalho, a empresa utiliza o Slack como plataforma de comunicação interna.

Foi solicitado para nós, profissionais de dados, o desenvolvimento de uma solução para extrair diariamente a cotação das moedas com as quais a empresa trabalha. São elas:

Dólar Americano (USD)
Libra Esterlina (GBP)
Euro (EUR)
Essa solução deve enviar as cotações para as pessoas responsáveis pelos gastos da empresa todos os dias às nove da manhã, no início do expediente.

Enviaremos essas informações numa tabela contendo a data e a cotação de cada uma das moedas mencionadas, separadas por colunas, conforme o seguinte exemplo:

data	USD	EUR	GBP
2023-05-22	0.201305	0.186176	0.161871
2023-05-21	0.200068	0.184865	0.160561
2023-05-20	0.199985	0.184767	0.160676
...	...	...	...
Também foi solicitada a criação de gráficos atualizados com o histórico de cotação dessas moedas num período de dois meses. Assim, conseguiremos avaliar se a cotação das moedas está em ascensão ou declínio — uma informação muito relevante para a nossa empresa.

Com isso, esperamos auxiliar o time responsável pelos gastos da empresa a ter previsões melhores acerca do consumo do orçamento.

A construção e execução de todo o pipeline para desenvolver essa solução será realizada com o Apache Airflow e o Databricks, mais especificamente na Cloud Azure. O Slack será o meio de envio da tabela e dos gráficos.

## conceito de taxa de cambio
A taxa de câmbio é um conceito que está relacionado ao valor de uma moeda em relação a outra moeda.

Imagine que você está planejando viajar para outro país e precisa trocar sua moeda local pela moeda do país que você vai visitar. Nesse caso, conhecer a taxa de câmbio para saber o quanto de dinheiro local você vai precisar para fazer a conversão da moeda será fundamental, ou seja, quantas unidades da moeda estrangeira você receberá em troca de sua moeda local.

Além disso, e entre outras características, a taxa de câmbio pode ser fixa ou flutuante. Uma taxa de câmbio fixa é determinada e controlada pelo governo ou autoridade monetária de um país. Nesse caso, o valor da moeda é mantido em um nível fixo em relação a uma outra moeda, geralmente uma moeda mais forte, através da intervenção do governo.

Por outro lado, uma taxa de câmbio flutuante é determinada pelo mercado, ou seja, pela oferta e demanda de moedas estrangeiras. Nesse caso, os valores das moedas podem variar ao longo do tempo de acordo com as condições econômicas e financeiras do país.

Em resumo, a taxa de câmbio desempenha um papel importante nas transações internacionais, como importações, exportações, investimentos estrangeiros e turismo. Ela afeta o custo dos produtos importados e exportados, bem como o poder de compra dos consumidores em relação a moedas estrangeiras.



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
export AIRFLOW_VERSION=2.6.1
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

## configurandp a azure

###alerta de custo
"Gerenciamento de custo". > "Orçamentos" >adicionar, colocar conta, periodo mensal valor 2$

criar conexão databricks databricks
-olhar pára pegar o tier mais barato  
iniciar workspace


## api com os dados

exchange api rates
https://apilayer.com/marketplace/exchangerates_data-api

apikey: JxSTDnwHcbXtWh67iqZjlcLBQUhlC7Wc

aposs criar o etl.
criar um job vinculando o arquivo da extração. 
Pra vincular o job no airflow precisa copiar o id do job criado

## configurando o airflow cm o job do databricks
https://docs.databricks.com/aws/en/jobs/how-to/use-airflow-with-jobs

iniciar o venv e airflow:
cd airflow-databricks
source curso_datAir/bin/activate
airflow standalone


abre o airflow no localHost:8080

abre o airflow dentro da base onde criamos a pasta dag
e abrir o vscode com code . 

criar arquivo extraindo-taxas.py (cod no arquivo)

## criando conexao entre databbricks e airflow
admin> connections : databricks_default

connectiontype: databricks
host = url da azure com o nome da conexão no databricks
login => deixar vazio para que qualquer usuario logue
password: gerar um access token no site do databricks em usuario>definicoes> programador>tokenAcesso
