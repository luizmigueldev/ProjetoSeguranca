from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Prontuario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#Criar um novo pronturario
class ProntuarioCreate(CreateView):
    model= Prontuario
    fields = ['nome',
              'dataNascimento',
              'contato',
              'pressaoArterial',
              'temperatura',
              'principaisSintomas',
              'dataInternacao',
              'dataAlta',
              'medicacao',
              'observacoesComplementares'
              ]
    template_name = 'telas/criarProntuario.html'
    success_url = reverse_lazy('lista_prontuario')

#Editar um prontuario
class ProntuarioUpdate(UpdateView):
    model= Prontuario
    fields = ['nome',
              'dataNascimento',
              'contato',
              'pressaoArterial',
              'temperatura',
              'principaisSintomas',
              'dataInternacao',
              'dataAlta',
              'medicacao',
              'observacoesComplementares'
              ]
    template_name = 'telas/editarProntuario.html'
    success_url = reverse_lazy('lista_prontuario')

#Excluir um prontuario
class ProntuarioDelete(DeleteView):
    model= Prontuario
    template_name = 'telas/excluirProntuario.html'
    success_url = reverse_lazy('lista_prontuario')

@login_required
def index(request):
    return render(request,'telas/index.html')

@login_required
def lista_prontuario(request):
    prontuarios = Prontuario.objects.all()
    return render(request,'telas/listaProntuario.html',{
        'prontuarios': prontuarios
    })

@login_required
def visualisar_prontuario(request,prontuario_id):
    prontuario = Prontuario.objects.get(id=prontuario_id)
    return render(request,'telas/visualisarProntuario.html', {
    'prontuario': prontuario
})

