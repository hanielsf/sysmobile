# Django
from django.urls import path

# Views PDF
from .views import PdfOrdemServico

app_name = 'pdf'
urlpatterns = [

    path('generate/pdf/os/<int:pk>', PdfOrdemServico.as_view(), name='generate_pdf'),

]

