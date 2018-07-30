# Django
from django import forms

# Local imports
from .models import Cliente


class ClienteForm(forms.ModelForm):
    pes_nome = forms.CharField(required=True, max_length=80,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    pes_cpf = forms.CharField(required=False, max_length=14,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    pes_rg = forms.CharField(required=False, max_length=20,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    pes_telefone = forms.CharField(required=False, max_length=16)
    pes_celular = forms.CharField(required=True, max_length=17)
    pes_email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    #  Uma classe inline para fornecer informações adicionais no formulário.
    class Meta:
        #  Fornecer uma associação entre ModelForm e um modelo
        model = Cliente
        fields = ('pes_nome', 'pes_cpf',
                  'pes_celular', 'pes_email',
                  'pes_rg', 'pes_telefone',)


