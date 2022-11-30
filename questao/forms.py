from django import forms
from questao.models import Questao


class QuestaoForm(forms.Form):
    id_questao = 0
    nome = forms.CharField(max_length=250)
    questoes = forms.MultipleChoiceField(
        # Must fill in choices and initial from the DB at runtime
        widget=forms.CheckboxSelectMultiple,
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(QuestaoForm, self).__init__(*args, **kwargs)
    
        self.site_id = kwargs.get('site_id')
        print("77777", self.site_id)

        # Get all the possible categories, you could use info from *args, **kwargs 
        # here to filter the list of categories if you wanted.  (i.e. to ones that 
        # are available to this user, etc.) 
        all_questoes = Questao.objects.get(id=1)
        self.fields['questoes'].choices = (
            [(str(c.id), c.descricao) for c in all_questoes.opcoes.all()])