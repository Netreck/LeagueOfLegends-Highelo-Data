from django.contrib import admin
from galeria.models import br_challenger_soloq
# Register your models here.
class ListandoPlayers(admin.ModelAdmin):
    list_display=("summoner_name","leaguePoints","role_most_played","monochampion")
    search_fields = ("summoner_name",)
    #list_filter=("categoria",)
   # list_editable=("publicada",)
    list_per_page=20
admin.site.register(br_challenger_soloq,ListandoPlayers)