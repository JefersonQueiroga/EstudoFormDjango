from django.shortcuts import render,redirect
from main.forms import AlunoForm,CalcularPesoForm
from django.views.generic import TemplateView,ListView
from main.models import Aluno
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
    return render(request,"index.html")

def logout_view(request):
     logout(request)
     return redirect('login')


@login_required
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

def pre_calculo(request):
    calculo = 0
    form_fabricio = CalcularPesoForm()
    
    if request.method=='POST':
        peso = float(request.POST['peso'])
        altura = float( request.POST['peso'] )
        calculo = peso + altura



    return render(request, 'form_peso.html', {'form': form_fabricio, 'calculo': calculo })