# Django imports
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

# Local
from .models import Dispositivo
from .forms import DispositivoForm
from apps.clientes.models import Cliente

# Terceiros
import sweetify


# DISPOSITIVO_ADD =======================================================================================
@login_required(login_url='/core/sign-in/')
def dispositivos_add(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST or None)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'dispositivos/dispositivo_add.html', {'form': form})
        model_instance = form.save(commit=False)
        model_instance.timestamp = timezone.now()
        model_instance.save()
        sweetify.success(request, 'Dispositivo cadastrado com sucesso!')
        return HttpResponseRedirect(reverse('dispositivos:dispositivos_detail', args=(model_instance.pk,)))
    else:
        form = DispositivoForm()
        return render(request, 'dispositivos/dispositivo_add.html', {'form': form})


# DISPOSITIVO_EDIT =======================================================================================
@login_required(login_url='/core/sign-in/')
def dispositivos_edit(request, pk):
    dispositivo = get_object_or_404(Dispositivo, pk=pk)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=dispositivo)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'dispositivos/dispositivo_edit.html', {'form': form})
        dispositivo = form.save(commit=False)
        dispositivo.timestamp = timezone.now()
        dispositivo.save()
        sweetify.success(request, 'Editado com Sucesso!')
        return HttpResponseRedirect(reverse('dispositivos:dispositivos_detail', args=(dispositivo.pk,)))
    else:
        form = DispositivoForm(instance=dispositivo)

    args = {'form': form, 'dispositivos': dispositivo}
    return render(request, 'dispositivos/dispositivo_edit.html', args)


# DISPOSITIVO_DELETE ======================================================================================
def dispositivos_delete(request, pk):
    dispositivo = get_object_or_404(Dispositivo, pk=pk)
    dispositivo.delete()
    sweetify.success(request, 'Dispositivo deletado com sucesso!')

    return redirect('/dispositivos')


# DISPOSITIVO_DETAIL ======================================================================================
@login_required(login_url='/core/sign-in/')
def dispositivos_detail(request, pk):
    msg = messages.get_messages(request)
    dispositivo = get_object_or_404(Dispositivo, pk=pk)

    args = {'dispositivo': dispositivo, 'message': msg}
    return render(request, 'dispositivos/dispositivo_detail.html', args)


# DISPOSITIVO_INDEX =======================================================================================
@login_required(login_url='/core/sign-in/')
def dispositivos_index(request):
    user = getattr(request, 'user', None)
    disp_list = Dispositivo.objects.all()
    paginator = Paginator(disp_list, 4)  # Exibir 10 objetos por pagina

    page = request.GET.get('page')
    try:
        dispositivos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dispositivos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dispositivos = paginator.page(paginator.num_pages)

    return render(request, 'dispositivos/dispositivo_list.html', {'dispositivos': dispositivos, 'user': user})


