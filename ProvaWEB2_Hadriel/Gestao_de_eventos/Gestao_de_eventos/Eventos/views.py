from django.shortcuts import render, redirect
from .forms import EventoForm

# Lista global para persistência em memória
eventos_db = [
    {'evento': 'Seminário de estatística', 'local': 'Laboratório 01'},
    {'evento': 'Semana da TI', 'local': 'Auditório'},
]

def home(request):
    # Lista os eventos ativos na Dashboard
    return render(request, 'Eventos/home.html', {'eventos': eventos_db})

def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # Extrai os dados e adiciona na lista global
            novo = {
                'evento': form.cleaned_data['nome_evento'],
                'local': form.cleaned_data['local_evento']
            }
            eventos_db.append(novo)
            return redirect('home') # Volta para a lista após cadastrar
    else:
        form = EventoForm()
    
    return render(request, 'Eventos/novo.html', {'form': form})