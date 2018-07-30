# Django
from django import forms

# Local imports
from .models import Dispositivo
from apps.clientes.models import Cliente
from .choices import MARCA_DISPOSITIVOS


class DispositivoForm(forms.ModelForm):
    marca = forms.ChoiceField(choices=MARCA_DISPOSITIVOS, required=True)
    modelo = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    imei = forms.IntegerField(required=True)
    url_img = forms.ImageField(required=False)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="----------", required=False)

    #  Uma classe inline para fornecer informações adicionais no formulário.
    class Meta:
        #  Fornecer uma associação entre ModelForm e um modelo
        model = Dispositivo
        fields = ('marca', 'modelo', 'imei', 'url_img', 'cliente')


