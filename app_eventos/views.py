from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Organizador
from .forms import EventoForm  # Importar o nosso novo formulário

# ... (mantém as tuas funções antigas de lista e detalhe aqui) ...

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda na base de dados!
            return redirect('lista_eventos')  # Volta para a página inicial
    else:
        form = EventoForm()
    
    return render(request, 'app_eventos/criar_evento.html', {'form': form})

def sobre(request):
    return render(request, 'app_eventos/sobre.html')