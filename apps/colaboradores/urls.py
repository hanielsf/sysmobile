# Django
from django.urls import include, path

# Views Cadastro
from . import views

app_name = 'colaboradores'
urlpatterns = [

    # CAD_CONTRATADO
    path('contratados/', views.contratado_index, name='contratado_index'),
    path('contratados/edit/<int:pk>', views.contratado_edit, name='contratado_edit'),
    path('contratados/add', views.contratado_add, name='contratado_add'),
    path('contratados/detail/<int:pk>', views.contratado_detail, name='contratado_detail'),
]
