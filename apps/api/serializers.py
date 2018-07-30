# coding=utf-8

# terceiros
from rest_framework import serializers

# local
from apps.dispositivos.models import Dispositivo
from apps.clientes.models import Cliente
from apps.servicos.models import OrdemServico


# ==================== MODEL DISPOSITIVO =============================
class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'


# ==================== MODEL CLIENTE =============================
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['pes_nome', 'pes_celular', 'pes_cpf']


# ==================== MODEL ORDEMSERVICO ============================
class OrdemServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdemServico
        fields = ['os_id', 'hospedagem', 'cliente']


# ==================== BUSCA GLOBAL =============================
class BuscaGlobalSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = OrdemServico
        fields = ['os_id', 'hospedagem', 'cliente', 'cliente_id']

    @staticmethod
    def to_native(obj):
        if isinstance(obj, Cliente):
            serializer = ClienteSerializer(obj)
        elif isinstance(obj, OrdemServico):
            serializer = OrdemServicoSerializer(obj)
        else:
            raise Exception("Nem um fragmento nem uma instância de usuário!")
        return serializer.data

