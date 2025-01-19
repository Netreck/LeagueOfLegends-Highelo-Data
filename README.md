# Projeto Pessoal- League of Data


## Intro

Em geral o Projeto é um site para analise de dados dos jogadores de League of Legends.

O Projeto tem o intuito de desenvolver minhas habilidades em Dados como ETL,PostgreSQL,DataVis,Automação de pipeline...

Exemplo atual do site:


<img width="1635" alt="Screenshot 2025-01-15 at 00 13 49" src="https://github.com/user-attachments/assets/be7be2c8-ec0f-4a4c-bac6-8c0ef003d6d9" />


## Processos

### Dados:
Sao coletados os dados dos top 200players do servidor Brasileiro (Challengers) por meio de três APIs todas da Riot Games.

Na primeira API LEAGUE-V4 são coletados  de cada um dos 200 jogadores do rank challenger (200 melhores) Puuid(rankunico) , Pontos de liga ,Vitorias , Derrotas. E assim criamos o primeiro DF_1

Depois para o segundo DF, usando o MATCH-V5, são coletadas os ids das 100 ultimas partidas de cada um dos jogadores challenger e também com usando MATCH-V5 são coletados dados de cada uma dessas partidas conectadas ao jogador indicado e armazenadas em outro DF que possue dados de 100 partidas de cada um dos jogadores, portanto, cerca de 20000 partidas.

Com base neste ultimo DF criado , escolhemos as colunas mais importantes para o MVP (Uma LeaderBoard) e criamos novas colunas que serao adicionadas ao nosso DF_1, nessas novas colunas junta-se informações de cada uma das partidas dos jogadores como por exemplo: Campeões mais jogados , posição preferida e etc.

Por ser um MVP criado apenas para solicitar um limite de API maior para Riot Games explorei apenas o básico de informações para a criação do leaderboard.

Após a criação do DF final ,  os dados são enviados para o PostgreSQL que esta hospedado na AmazonRDS.

### Deploy:
Utilizando Django liguei com o banco de dados e organizei as informações no formato de uma LeaderBoard


