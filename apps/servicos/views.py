# Django imports
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

# Local
from qr_code.qrcode.serve import make_qr_code_url
from qr_code.qrcode.utils import QRCodeOptions

from apps.clientes.models import Cliente
from .models import OrdemServico
from .forms import OrdemServicoForm
from apps.dispositivos.models import Dispositivo

# Terceiros
import sweetify


# ORDEM_SERVICO_ADD =======================================================================================
@login_required(login_url='/core/sign-in/')
def ordemservicos_add(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST or None)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'servicos/os/os_add.html', {'form': form})
        model_instance = form.save(commit=False)
        model_instance.timestamp = timezone.now()
        model_instance.save()
        sweetify.success(request, 'Ordem de Serviço criada com sucesso!')
        return HttpResponseRedirect(reverse('servicos:ordemservicos_detail', args=(model_instance.pk,)))
    else:
        form = OrdemServicoForm()
        return render(request, 'servicos/os/os_add.html', {'form': form})


# ORDEM_SERVICO_EDIT =======================================================================================
@login_required(login_url='/core/sign-in/')
def ordemservicos_edit(request, pk):
    ordemservico = get_object_or_404(OrdemServico, pk=pk)

    if request.method == "POST":
        form = OrdemServicoForm(request.POST, instance=ordemservico)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'servicos/os/os_edit.html', {'form': form})
        ordemservico = form.save(commit=False)
        ordemservico.timestamp = timezone.now()
        ordemservico.save()
        sweetify.success(request, 'Editado com Sucesso!')
        return HttpResponseRedirect(reverse('servicos:ordemservicos_detail', args=(ordemservico.pk,)))
    else:
        form = OrdemServicoForm(instance=ordemservico)

    args = {'form': form, 'ordemservico': ordemservico}
    return render(request, 'servicos/os/os_edit.html', args)


# ORDEM_SERVICO_DELETE ======================================================================================
def ordemservicos_delete(request, pk):
    dispositivo = get_object_or_404(OrdemServico, pk=pk)
    dispositivo.delete()
    sweetify.success(request, 'O.S deletada com sucesso!')

    return redirect('/servicos/os')


# ORDEM_SERVICO_DETAIL ======================================================================================
@login_required(login_url='/core/sign-in/')
def ordemservicos_detail(request, pk):
    msg = messages.get_messages(request)
    ordemservico = get_object_or_404(OrdemServico, pk=pk)

    options_qr = QRCodeOptions(size='t', border=6, error_correction='L')
    qr_url = make_qr_code_url("URL:https://excelencia.online/c/" + str(ordemservico.os_id),
                              qr_code_options=options_qr)

    args = {'ordemservico': ordemservico, 'qr_url': qr_url,  'message': msg}
    return render(request, 'servicos/os/os_detail.html', args)


# ORDEM_SERVICO_INDEX =======================================================================================
@login_required(login_url='/core/sign-in/')
def ordemservicos_index(request):
    user = getattr(request, 'user', None)
    os_list = OrdemServico.objects.select_related('cliente', 'dispositivos').exclude(status=9)

    paginator = Paginator(os_list, 4)  # Exibir 10 objetos por pagina

    page = request.GET.get('page')

    try:
        ordensservico = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ordensservico = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ordensservico = paginator.page(paginator.num_pages)

    args = {'ordensservico': ordensservico, 'user': user}
    return render(request, 'servicos/os/os_list.html', args)


