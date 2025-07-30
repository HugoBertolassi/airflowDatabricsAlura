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

# outras infos
O Glob Patterns é um padrão comum usado em sistemas Unix e similares ao Unix, onde caracteres especiais são usados para corresponder a um conjunto de arquivos ou diretórios com base em um padrão específico. O Spark suporta o uso desses padrões para reconhecer caminhos ao ler ou também gravar dados. Existem semelhanças superficiais com o uso de expressões regulares (RegEx), mas é outro tipo de padrão.
* (asterisco): Corresponde a qualquer sequência de caracteres em um único nível de diretório. Por exemplo, "/diretorio1//.csv" corresponderá a todos os arquivos de extensão “.csv” em qualquer diretório dentro de "/diretorio1/". É o mesmo padrão utilizado na leitura dos arquivos realizada na aula anterior.

? (ponto de interrogação): Corresponde a um único caractere em um nome de arquivo ou diretório. Por exemplo, "/diretorio1/arquivo?.csv" corresponderá a "/diretorio1/arquivo1.csv" e "/diretorio1/arquivo2.csv", mas não a "/diretorio1/arquivo.csv" nem "/diretorio1/arquivo10.csv", porque possui mais de um caractere entre os fragmentos de texto “arquivo” e “.csv”.

[ ] (colchetes): Corresponde a qualquer caractere dentro dos colchetes. Por exemplo, "/diretorio1/arquivo[12].csv" corresponderá ao caminho "/diretorio1/arquivo1.csv" e "/diretorio1/arquivo2.csv", mas não a "/diretorio1/arquivo3.csv" nem "/diretorio1/arquivo.csv".
