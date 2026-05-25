from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('organizadores/', views.lista_organizadores, name='lista_organizadores'),
    # Novas páginas:
    path('criar-evento/', views.criar_evento, name='criar_evento'),
    path('sobre/', views.sobre, name='sobre'),
]