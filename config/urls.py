from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from apps.core import views as main_views
from ajax_select import urls as ajax_select_urls
from qr_code import urls as qr_code_urls
from apps.api.router import router


urlpatterns = [
    # Dashboard Principal
    path('', main_views.dashboard, name='dashboard'),

    # ADMIN: Apenas para administradores
    path('ediclei/', admin.site.urls),

    # APP: Core (Principal)
    path('core/', include('apps.core.urls')),

    # APPS: Local
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('empregador/', include('apps.empregador.urls')),
    path('dispositivos/', include('apps.dispositivos.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('servicos/', include('apps.servicos.urls')),
    path('pdf/', include('apps.pdf.urls')),

    # API
    path('api/', include('apps.api.urls')),

    path('ajax_select/', include(ajax_select_urls)),
    path('qr_code/', include(qr_code_urls, namespace="qr_code")),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
