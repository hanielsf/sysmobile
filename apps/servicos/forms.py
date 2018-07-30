# Django
from django import forms

# Local imports
from .models import OrdemServico
from apps.clientes.models import Cliente
from apps.dispositivos.models import Dispositivo
from .choices import STATUS, TIPO_SERVICOS, ACESSORIOS_DISPOSITIVOS

# terceiros
from djmoney.forms.fields import MoneyField


class OrdemServicoForm(forms.ModelForm):
    acessorios = forms.MultipleChoiceField(required=False, choices=ACESSORIOS_DISPOSITIVOS,
                                           widget=forms.CheckboxSelectMultiple())
    tipo_servico = forms.ChoiceField(choices=TIPO_SERVICOS, required=True)
    descricao = forms.CharField(required=False, max_length=300,
                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    status = forms.ChoiceField(choices=STATUS, required=True)
    hospedagem = forms.CharField(required=False, max_length=4)

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Selecione um cliente...",
                                     widget=forms.Select(attrs={'onchange': 'getDispositivo()'}))
    dispositivos = forms.ModelChoiceField(empty_label="<-----------", queryset=Dispositivo.objects.all())
    orcamento = MoneyField(required=False, default_amount=0, max_digits=10,
                           localize=True, decimal_places=2, default_currency='BRL')

    #  Uma classe inline para fornecer informações adicionais no formulário.
    class Meta:
        #  Fornecer uma associação entre ModelForm e um modelo
        model = OrdemServico
        fields = ('acessorios', 'tipo_servico', 'descricao', 'status',
                  'cliente', 'dispositivos', 'orcamento', 'hospedagem')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dispositivos'].queryset = Dispositivo.objects.none()

        if 'cliente' in self.data:
            try:
                cliente_id = int(self.data.get('cliente'))
                self.fields['dispositivos'].queryset = Dispositivo.objects.filter(cliente_id=cliente_id).order_by(
                    'modelo')
            except (ValueError, TypeError):
                pass  #
        elif self.instance.pk:
            self.fields['dispositivos'].queryset = self.instance.cliente.dispositivo_set.order_by('modelo')
