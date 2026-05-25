from django.shortcuts import render, get_object_or_404
from .models import Evento, Organizador

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'app_eventos/lista_eventos.html', {'eventos': eventos})

def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'app_eventos/detalhe_evento.html', {'evento': evento})

def lista_organizadores(request):
    organizadores = Organizador.objects.all()
    return render(request, 'app_eventos/lista_organizadores.html', {'organizadores': organizadores})