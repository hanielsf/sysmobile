# Django imports
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

# Local
from .models import Contratado
from .forms import ContratadoForm

# Terceiros
import sweetify


# CONTRATADO_ADD =======================================================================================
@login_required(login_url='/core/sign-in/')
def contratado_add(request):
    if request.method == 'POST':
        form = ContratadoForm(request.POST or None)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'colaboradores/contratados/contratado_add.html', {'form': form})
        model_instance = form.save(commit=False)
        model_instance.timestamp = timezone.now()
        model_instance.save()
        sweetify.success(request, 'Funcionario cadastrado com sucesso!')
        return HttpResponseRedirect(reverse('colaboradores:contratado_detail', args=(model_instance.pk,)))
    else:
        form = ContratadoForm()
        return render(request, 'colaboradores/contratados/contratado_add.html', {'form': form})


# CONTRATADO_EDIT =======================================================================================
@login_required(login_url='/core/sign-in/')
def contratado_edit(request, pk):
    contratado = get_object_or_404(Contratado, pk=pk)
    if request.method == "POST":
        form = ContratadoForm(request.POST, instance=contratado)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'colaboradores/contratados/contratado_edit.html', {'form': form})
        contratado = form.save(commit=False)
        contratado.timestamp = timezone.now()
        contratado.save()
        sweetify.success(request, 'Editado com Sucesso!')
        return HttpResponseRedirect(reverse('colaboradores:contratado_detail', args=(contratado.pk,)))
    else:
        form = ContratadoForm(instance=contratado)

    args = {'form': form, 'contratados': contratado}
    return render(request, 'colaboradores/contratados/contratado_edit.html', args)


# CONTRATADO_DELETE ======================================================================================
def contratado_delete(request, pk):
    contratado = Contratado.objects.filter(pk=pk)
    contratado.delete()
    return redirect("contratado_index")


# CONTRATADO_DETAIL ======================================================================================
@login_required(login_url='/core/sign-in/')
def contratado_detail(request, pk):
    msg = messages.get_messages(request)
    contratado = get_object_or_404(Contratado, pk=pk)

    args = {'contratado': contratado, 'message': msg}
    return render(request, 'colaboradores/contratados/contratado_detail.html', args)


# CONTRATADO_INDEX =======================================================================================
@login_required(login_url='/core/sign-in/')
def contratado_index(request):
    user = getattr(request, 'user', None)
    pes_list = Contratado.objects.all()
    paginator = Paginator(pes_list, 10)  # Exibir 10 objetos por pagina

    page = request.GET.get('page')
    try:
        contratados = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contratados = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contratados = paginator.page(paginator.num_pages)

    return render(request, 'colaboradores/contratados/contratado_list.html', {'contratados': contratados, 'user': user})


