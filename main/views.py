from django.shortcuts import render
from main.forms import AlunoForm

def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST) 
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()

    return render(request,'form.html', { 'form' : form})

