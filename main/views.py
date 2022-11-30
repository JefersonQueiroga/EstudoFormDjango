from django.shortcuts import render
from main.forms import AlunoForm
from django.views.generic import TemplateView,ListView
from main.models import Aluno

def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST) 
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()

    return render(request,'form.html', { 'form' : form})


def form_top(request):
    form = AlunoForm(request.POST or None)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST) 
        if form.is_valid():
            form.save()
            form = AlunoForm()
      
    return render(request,'formtop.html',{ 'form' : form})

def pagina_inicial(request):
    return render(request,"index.html")


class TelaQuemSomos(TemplateView):
    template_name = 'quemsomos.html'

class ListAlunosView(ListView):
    template_name = 'lista_alunos.html'
    model = Aluno
