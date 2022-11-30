from django import forms
from main.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        fields= '__all__'   

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date'}),
        }

class CalcularPesoForm(forms.Form):
    peso = forms.FloatField()
    altura = forms.FloatField()
    object = forms.Textarea()


