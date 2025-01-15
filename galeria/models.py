from django.db import models


class br_challenger_soloq(models.Model):
    summonerId = models.CharField(max_length=50, unique=True)  # ID do invocador
    accountId = models.CharField(max_length=50)  # ID da conta
    puuid =  models.CharField(max_length=50,primary_key = True)
    summoner_name = models.CharField(max_length=50)
    profileIconId = models.IntegerField()  # Ícone do perfil
    revisionDate = models.BigIntegerField()  # Data da última revisão
    summonerLevel = models.IntegerField()  # Nível do invocador
    tier = models.CharField(max_length=50)  # Tier (ex: Bronze, Silver, Gold, etc.)
    queue = models.CharField(max_length=50)  # Fila (ex: solo, flex)
    leaguePoints = models.IntegerField()  # Pontos de liga
    wins = models.IntegerField()  # Quantidade de vitórias
    losses = models.IntegerField()  # Quantidade de derrotas
    veteran = models.BooleanField()  # Indica se o invocador é veterano
    inactive = models.BooleanField()  # Indica se o invocador está inativo
    freshBlood = models.BooleanField()  # Indica se o invocador é novo
    hotStreak = models.BooleanField()  # Indica se o invocador está em streak quente
    winrate = models.FloatField()  # Taxa de vitórias
    deaths_mean = models.FloatField()  # Média de mortes
    game_duration_mean = models.FloatField()  # Duração média das partidas
    top2_champion = models.CharField(max_length=100)  # Top 2 campeao
    enemy_missing_pings_mean = models.FloatField()  # Média de pings de inimigos ausentes
    monochampion = models.CharField(max_length=100)  # Campeão monocromático
    role_most_played = models.CharField(max_length=50)  # Função mais jogada
    top3_champion = models.CharField(max_length=100, null=True, blank=True)  # Top 3 campeao
    top1_champion = models.CharField(max_length=100)  # Top 1 campeão
    class Meta:
        db_table = '"soloq"."br_challenger_soloq"' 


    def __str__(self):
        return f'{self.summoner_name} - {self.leaguePoints}'