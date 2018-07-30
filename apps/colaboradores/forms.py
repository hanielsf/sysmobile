# Django
from django import forms

# Local imports
from .models import Contratado
from apps.empregador.models import Estabelecimento, Lotacao, Funcao, Sindicato


class ContratadoForm(forms.ModelForm):
    pes_nome = forms.CharField(required=True, max_length=80,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    pes_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    con_matricula = forms.CharField(required=True, max_length=30, min_length=3,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    estabelecimento = forms.ModelChoiceField(queryset=Estabelecimento.objects.all(),
                                             empty_label="----------")
    lotacao = forms.ModelChoiceField(queryset=Lotacao.objects.all(), empty_label="----------")
    funcao = forms.ModelChoiceField(queryset=Funcao.objects.all(), empty_label="----------")
    sindicato = forms.ModelChoiceField(queryset=Sindicato.objects.all(), empty_label="----------")

    #  Uma classe inline para fornecer informações adicionais no formulário.
    class Meta:
        #  Fornecer uma associação entre ModelForm e um modelo
        model = Contratado
        fields = ('pes_nome', 'pes_email', 'con_matricula',
                  'estabelecimento', 'lotacao', 'funcao',
                  'sindicato')
