from django.contrib import admin
from .models import Organizador, Evento

# Isto serve para que o painel de administração do Django reconheça as nossas tabelas
admin.site.register(Organizador)
admin.site.register(Evento)