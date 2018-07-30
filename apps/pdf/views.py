from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.utils import timezone
from qr_code.qrcode.maker import make_embedded_qr_code

from qr_code.qrcode.serve import make_qr_code_url
from qr_code.qrcode.utils import QRCodeOptions
from qr_code.views import make_qr_code_image

from .pdf import Render

from apps.servicos.models import OrdemServico


class PdfOrdemServico(View):

    def get(self, request, pk):
        ordemservico = get_object_or_404(OrdemServico, pk=pk)
        today = timezone.now()

        options_qr = QRCodeOptions(size='t', border=6, image_format='png', error_correction='L')
        qr_code = make_embedded_qr_code("URL:https://excelencia.online/c/" + str(ordemservico.os_id),
                                        qr_code_options=options_qr)

        params = {
            'today': today,
            'ordemservico': ordemservico,
            'qr_code': qr_code,
            'request': request
        }

        return Render.render('pdf/imprimir_os.html', params)
