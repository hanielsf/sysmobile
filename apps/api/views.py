from itertools import chain

from django.db.models import Q

from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *

from apps.clientes.models import Cliente
from apps.dispositivos.models import Dispositivo
from apps.servicos.models import OrdemServico


# ====================== ORDEMSERVICO VIEWSET =============================
class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer


# ====================== GET CLIENTE VIEW =============================
@api_view(['GET'])
def get_cliente(request, sid):
    clienteobj = Cliente.objects.filter(ordemservico=sid)
    cliente_serializer = ClienteSerializer(clienteobj, many=True)
    response = Response(cliente_serializer.data)
    return Response(response.data, status=status.HTTP_200_OK)


# ====================== GET DISPOSITIVO VIEW =============================
@api_view(['GET'])
def get_dispositivo(request, cliente_id):
    dispositivoobj = Dispositivo.objects.filter(cliente_id=cliente_id)
    dispositivo_serializer = DispositivoSerializer(dispositivoobj, many=True)
    response = Response(dispositivo_serializer.data)
    return Response(response.data, status=status.HTTP_200_OK)


# ====================== BUSCA GLOBAL LISTAPIVIEW =============================
class BuscaGlobalList(generics.ListAPIView):
    serializer_class = BuscaGlobalSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        ordenservico = OrdemServico.objects.filter(
            Q(os_id__icontains=query) | Q(hospedagem__icontains=query))
        cliente = Cliente.objects.filter(
            Q(pes_nome__icontains=query) | Q(pes_celular__icontains=query) | Q(pes_cpf__icontains=query))

        all_results = list(chain(ordenservico, cliente))
        all_results.sort(key=lambda x: x.created_at)
        return all_results


