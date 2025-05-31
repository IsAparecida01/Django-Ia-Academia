from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClientesForm, RelatorioDesempenhoForm
from .models import ClientesModel, RelatorioDesempenho
from django.http import HttpRequest
import pickle
import joblib
from sklearn.preprocessing import LabelEncoder
import pandas as pd



def clientes_home(request):

     contexto = {
          "clientes": ClientesModel.objects.all()
      }
     return render(request, 'clientes/home.html', contexto)


def clientes_adicionar(request:HttpRequest):
     
     if request.method == "POST": 
      formulario = ClientesForm(request.POST)
      if formulario.is_valid():
         formulario.save()
         return redirect("clientes:home")
     
     contexto = { 
          "form": ClientesForm
     }

     return render(request, 'clientes/adicionar.html', contexto)

def clientes_remover(request:HttpRequest, id): 
    cliente = get_object_or_404(ClientesModel, id=id)
    cliente.delete()
    return redirect("clientes:home")

def clientes_editar(request:HttpRequest, id):
    cliente = get_object_or_404(ClientesModel, id=id)
    if request.method == "POST": 
        formulario = ClientesForm(request.POST, instance=cliente)
        if formulario.is_valid(): 
            formulario.save()
            return redirect("clientes:home")
    formulario = ClientesForm(instance=cliente)
    context = {
        'form': formulario
    }
    return render(request, 'clientes/editar.html', context)


with open('ml/modelo_desistencia.pkl', 'rb') as f:
    modelo = pickle.load(f)

modelo = joblib.load('ml/modelo_desistencia.pkl')
le_genero = LabelEncoder().fit(['F', 'M', 'O'])  # igual ao usado no treino
le_estacao = LabelEncoder().fit(['Verão', 'Outono', 'Inverno', 'Primavera'])

def clientes_desempenho(request, id):
    cliente = ClientesModel.objects.get(id=id)
    relatorio = RelatorioDesempenho.objects.filter(cliente=cliente).last()

    if relatorio:
        entrada = pd.DataFrame([{
            'genero': le_genero.transform([cliente.genero])[0],
            'idade': cliente.idade,
            'frequencia': relatorio.frequencia,
            'estacao': le_estacao.transform([relatorio.estacao])[0],
            'objetivo_alcancado': int(relatorio.objetivo_alcancado),
            'satisfacao': relatorio.satisfacao,
            'lesoes': int(relatorio.lesoes)
        }])

        entrada = entrada[['genero', 'idade', 'frequencia', 'estacao', 'objetivo_alcancado', 'satisfacao', 'lesoes']]

        previsao = modelo.predict_proba(entrada)[0][1] * 100  # chance de desistência

        relatorio.chance_desistencia = previsao
        relatorio.save()

        return render(request, 'clientes/desempenho.html', {'cliente': cliente, 'relatorio': relatorio, 'chance': round(previsao, 2)})
    
    return render(request, 'clientes/desempenho.html', {'cliente': cliente, 'relatorio': None})






def registrar_desempenho(request, id):
    cliente = get_object_or_404(ClientesModel, id=id)

    if request.method == 'POST':
        form = RelatorioDesempenhoForm(request.POST)
        if form.is_valid():
            desempenho = form.save(commit=False)
            desempenho.cliente = cliente
            desempenho.save()
            return redirect('clientes:desempenho', id=id)
    else:
        form = RelatorioDesempenhoForm()

    return render(request, 'clientes/registrar_desempenho.html', {
        'form': form,
        'cliente': cliente
    })

