from django.shortcuts import render
from questao.forms import QuestaoForm
# Create your views here.

def form_questao(request):
    form = QuestaoForm(site_id=1)
    
    return render(request,'questoes.html',{'form':form})