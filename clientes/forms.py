from django import forms 
from .models import ClientesModel
from .models import RelatorioDesempenho

class ClientesForm(forms.ModelForm):
    class Meta: 
        model = ClientesModel
        fields = ['nome', 'genero', 'idade', 'email', 'telefone', 'plano']


class RelatorioDesempenhoForm(forms.ModelForm):
    class Meta:
        model = RelatorioDesempenho
        exclude = ['cliente', 'chance_desistencia', 'data']

        