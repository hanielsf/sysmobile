from __future__ import unicode_literals
from django.db.models import Q
from django.utils.html import escape
from apps.clientes.models import Cliente
from ajax_select import LookupChannel


class ClienteLookup(LookupChannel):
    model = Cliente

    def get_query(self, q, request):
        return Cliente.objects.filter(Q(pes_nome__icontains=q) | Q(pes_cpf__istartswith=q)).order_by('pes_cpf')

    def get_result(self, obj):
        """ result is the simple text that is the completion of what the person typed """
        return obj.pes_nome

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return "%s<div><i>%s</i></div>" % (escape(obj.pes_nome), escape(obj.pes_cpf))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return "%s<div><i>%s</i></div>" % (escape(obj.pes_nome), escape(obj.pes_cpf))

