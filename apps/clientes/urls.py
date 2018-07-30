# Django
from django.urls import include, path

# Views Dispositivos
from . import views

app_name = 'clientes'
urlpatterns = [

    # CAD_Clientes
    path('', views.clientes_index, name='clientes_index'),
    path('edit/<int:pk>', views.clientes_edit, name='clientes_edit'),
    path('add', views.clientes_add, name='clientes_add'),
    path('detail/<int:pk>', views.clientes_detail, name='clientes_detail'),
    path('delete/<int:pk>', views.clientes_delete, name='clientes_delete'),
]
