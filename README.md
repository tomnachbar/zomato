## 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
O Ceo da empresa solicita que seja criada uma ferramenta para a análise de dados através de dashboards interativos para filtrar e ter as melhores métricas para a tomada de decisão. As perguntas de negócio informadas foram:

Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

Pais
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
Distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
Entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
Reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
Registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?


Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os
restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?


Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

## 2. Premissas assumidas para a análise
1. A análise foi realizada com dados gerais sem um prazo pré-determinado.
2. Marketplace foi o modelo de negócio assumido.
3. As 3 principais visões do negócio foram: Visão por País, Visão por Cidades e Visão por tipos de Culinárias distintas.
4. Foi utilizado uma base de dados públicas da plataforma Kaggle através do link:https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv


## 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
Visão por País, Visão por Cidades e Visão por tipos de Culinárias distintas. Cada visão é representada pelo seguinte conjunto de métricas:

. Visão por País
a. Quantidade de restaurantes registrados por País
b. Quantidade de cidades registrados por País
c. Média de Avaliações feitas por País
d. Média de preço de prato para duas pessoas

. Visão por Cidades
a. Top 10 Cidades com mais restaurantes na Base de Dados
b. Top 7 Cidades com Restaurantes com média de avaliação superior a 4.0
c. Top 7 Cidades com Restaurantes com média de avaliação inferior a 2.5
d. Top 10 Cidades com mais tipos de culinárias distintas

. Visão por Tipo Culinário
a. O melhor restaurante do tipo italiano.
b. O melhor restaurante do tipo americano.
c. O melhor restaurante do tipo árabe.
d. O melhor restaurante do tipo japonês.
e. O melhor restaurante do tipo brasileiro.
f. Tabela com os 10 melhores restaurantes ranqueados por nota média de avaliação.
g. Top 10 melhores tipos de culinária.
h. Top 10 piores tipos de culinária.

## 4. Top 3 Insights de dados
1. Turquia e Indonésia apesar de não estarem na lista das top 10 cidades com mais restaurantes cadastrados, aparecem na Top 07 cidades com restaurantes avaliados acima de 4.0 pontos.
2. A Inglaterra apesar de estar apenas em 4º lugar no ranking de mais restaurantes cadastrados, aparece nas quatro primeiras colocações com cidades em número de culinária distintas.
3. O Brasil é o único País no ranking top 10 melhores restaurantes que possui um restaurante com a própria culinária, os demais países aparecem com culinárias distintas.

## 5. O produto final do projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://tomnachbar-zomato.streamlit.app/

## 6. Conclusão
O objetivo do projeto foi criar um dashboard interativo para que pudesse ser realizado consultas com tipos distintos de culinária e países.
Podemos concluir que apesar de países muito populosos aparecem diversas vezes no ranking como Índia, EUA e Emirados Árabes, as avaliações dos restaurantes, bem como seus tipos culinários não são tão apreciados de modo geral pelos consumidores, tendo notas relativamente baixas nas avaliações. Curiosamente observamos que na Inglaterra apesar de não ter tantos restaurantes registrados por cidade, a maioria deles são bem avaliados e possuem uma grande diversidade culinária.

## 7. Próximo passos

1. Para um próximo projeto sugiro a inclusão de métricas voltadas por qual tipo de consumidor foram feitas as avaliações, a fim de identificar os públicos dos restaurantes.
2. Criar novos filtros.
3. Adicionar a visão por gênero.

## 8. Ferramentas Utilizadas para o Projeto

GitHub
Visual Studio Code
Python
Pandas
Streamlit

