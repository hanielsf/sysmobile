# Django
from django.urls import path

# Views API
from apps.api.views import BuscaGlobalList
from . import views

app_name = 'api'


urlpatterns = [

    # http://server/api/busca/?q={sua busca}
    path('busca/', BuscaGlobalList.as_view(), name='busca'),

    path('get_cliente/<int:sid>/', views.get_cliente, name='get_cliente'),
    path('get_dispositivo/<int:cliente_id>/', views.get_dispositivo, name='get_dispositivo'),

    # OrdemServico
    path('os/', views.CreateViewOrdemServico.as_view()),
    path('os/<int:pk>/', views.DetailsViewOrdemServico.as_view()),
]
