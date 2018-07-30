# Django
from django.urls import include, path

# Views Servicos
from . import views

app_name = 'servicos'
urlpatterns = [

    # CAD_OS
    path('os/', views.ordemservicos_index, name='ordemservicos_index'),
    path('os/edit/<int:pk>', views.ordemservicos_edit, name='ordemservicos_edit'),
    path('os/add/', views.ordemservicos_add, name='ordemservicos_add'),
    path('os/detail/<int:pk>', views.ordemservicos_detail, name='ordemservicos_detail'),
    path('os/delete/<int:pk>', views.ordemservicos_delete, name='ordemservicos_delete'),

]
