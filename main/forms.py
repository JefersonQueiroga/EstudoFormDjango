from django import forms
from main.models import Aluno


class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'



class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        fields= '__all__'   

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date'}),
        }
