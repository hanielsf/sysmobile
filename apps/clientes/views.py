# Django imports
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

# Local
from .models import Cliente
from .forms import ClienteForm
from apps.dispositivos.models import Dispositivo

# Terceiros
import sweetify


# CLIENTE_ADD =======================================================================================
@login_required(login_url='/core/sign-in/')
def clientes_add(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'clientes/cliente_add.html', {'form': form})
        model_instance = form.save(commit=False)
        model_instance.timestamp = timezone.now()
        model_instance.save()
        sweetify.success(request, 'Cliente cadastrado com sucesso!')
        return HttpResponseRedirect(reverse('dispositivos:dispositivos_add'))
    else:
        form = ClienteForm()
        return render(request, 'clientes/cliente_add.html', {'form': form})


# CLIENTE_EDIT =======================================================================================
@login_required(login_url='/core/sign-in/')
def clientes_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if not form.is_valid():
            sweetify.error(request, 'Ha algum erro no preenchimento dos campos!', persistent='OK')
            return render(request, 'clientes/cliente_edit.html', {'form': form})
        cliente = form.save(commit=False)
        cliente.timestamp = timezone.now()
        cliente.save()
        sweetify.success(request, 'Editado com Sucesso!')
        return HttpResponseRedirect(reverse('clientes:clientes_detail', args=(cliente.pk,)))
    else:
        form = ClienteForm(instance=cliente)

    args = {'form': form, 'clientes': cliente}
    return render(request, 'clientes/cliente_edit.html', args)


# CLIENTE_DELETE ======================================================================================
def clientes_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    sweetify.success(request, 'Cliente deletado com sucesso!')

    return redirect('/clientes')


# CLIENTE_DETAIL ======================================================================================
@login_required(login_url='/core/sign-in/')
def clientes_detail(request, pk):
    msg = messages.get_messages(request)
    cliente = get_object_or_404(Cliente, pk=pk)

    args = {'cliente': cliente, 'message': msg}
    return render(request, 'clientes/cliente_detail.html', args)


# CLIENTE_INDEX =======================================================================================
@login_required(login_url='/core/sign-in/')
def clientes_index(request):
    user = getattr(request, 'user', None)
    cliente_list = Cliente.objects.all()
    paginator = Paginator(cliente_list, 5)  # Exibir 10 objetos por pagina

    page = request.GET.get('page')
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'clientes/cliente_list.html', {'clientes': clientes, 'user': user})


