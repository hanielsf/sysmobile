# Django
from django.urls import include, path

# Views Dispositivos
from . import views

app_name = 'dispositivos'
urlpatterns = [

    # CAD_Dispositivos
    path('', views.dispositivos_index, name='dispositivos_index'),
    path('edit/<int:pk>', views.dispositivos_edit, name='dispositivos_edit'),
    path('add', views.dispositivos_add, name='dispositivos_add'),
    path('detail/<int:pk>', views.dispositivos_detail, name='dispositivos_detail'),
    path('delete/<int:pk>', views.dispositivos_delete, name='dispositivos_delete'),
]
