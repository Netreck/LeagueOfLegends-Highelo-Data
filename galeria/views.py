from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from galeria.models import br_challenger_soloq

def index(request):
    player_data= br_challenger_soloq.objects.order_by("-leaguePoints")
    return render(request,'galeria/index.html',{"player_data":player_data})

def imagem(request,foto_id):
    #fotografia=get_object_or_404(Fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html',{"fotografia":0})

def buscar(request):  
    #fotografias= Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
       

    return render(request,"galeria/buscar.html",{"cards":fotografias})

