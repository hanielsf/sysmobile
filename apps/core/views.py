#  Django
import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render, redirect

# local
from apps.servicos.models import OrdemServico

#  Terceiros
import sweetify


#  DASHBOARD_PRINCIPAL ===============================================================================
@login_required(login_url='/core/sign-in/')
def dashboard(request):
    storage = messages.get_messages(request)
    user = getattr(request, 'user', None)

    hoje = datetime.date.today()

    os_abertas = OrdemServico.objects.filter(Q(status=1)).count()
    os_prontas = OrdemServico.objects.filter(Q(status=8)).count()
    os_entregues = OrdemServico.objects.filter(Q(status=9)).count()
    os_atrasadas = OrdemServico.objects.filter(created_at__day=-30 + hoje.day).count()

    args = {'user': user, 'message': storage, 'os_abertas': os_abertas,
            'os_prontas': os_prontas, 'os_atradadas': os_atrasadas, 'os_entregues': os_entregues}
    return render(request, 'core/dashboard.html', args)


#  ===================================================================================================


#  LOGIN_USER =======================================================================================
def login_user(request):
    if not request.method == 'POST':
        return render(request, 'core/sign_in.html')
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/')
    sweetify.error(request, 'Usuário ou Senha inválidos!', persistent='OK')
    return render(request, 'core/sign_in.html')
#  ===================================================================================================


#  LOGOUT_USER =======================================================================================
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'core/sign_in.html')
#  ===================================================================================================
