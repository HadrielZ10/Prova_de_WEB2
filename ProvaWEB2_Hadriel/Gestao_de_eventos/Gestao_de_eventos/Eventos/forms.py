from django import forms

class EventoForm(forms.Form):
    nome_evento = forms.CharField(label="Evento", max_length=100)
    local_evento = forms.CharField(label="Local", max_length=100)