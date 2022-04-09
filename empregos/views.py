from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Emprego
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required

# Faz com que views só sejam acessadas caso usuários estejam logados
@login_required(login_url='/auth/login')
def encontrar_emps(request):
    print(request.user.id)
    if request.method == 'GET':
        #print(emps)
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')
        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_minimo')
        categoria = request.GET.get('categoria')
    
        # Se um dos filtros foi usado
        if preco_minimo or preco_maximo or prazo_minimo or prazo_maximo or categoria:
            if not preco_minimo:
                preco_minimo = 0

            if not preco_maximo:
                preco_maximo = 999999

            if not prazo_minimo:
                prazo_minimo = datetime(year=1900, month=1, day=1)

            if not prazo_maximo:
                prazo_maximo = datetime(year=3000, month=1, day=1)

            if categoria == 'D':
                categoria = ['D',]
            elif categoria == 'EV':
                categoria = ['EV',]
            else:
                categoria = ['EV','D']
            # O categoria_in no filtro abaixo verifica se categoria está numa lista 

            # .exclude(criador=)
            emps = Emprego.objects.filter(preco__gte=preco_minimo)\
                .filter(preco__lte=preco_maximo)\
                .filter(prazo_entrega__gte=prazo_minimo)\
                .filter(prazo_entrega__lte=prazo_maximo)\
                .filter(categoria__in=categoria)\
                .filter(reservado=False)
        else:
            emps = Emprego.objects.filter(reservado = False)


        return render(request, 'encontrar_emps.html',{'emps':emps})

@login_required(login_url='/auth/login')
def aceitar_emp(request, id):
    emp = Emprego.objects.get(id=id)
    emp.profissional = request.user
    emp.reservado = True
    emp.save()
    return redirect('/')

@login_required(login_url='/auth/login')
def perfil(request):
    if request.method == "GET":
        emps = Emprego.objects.filter(profissional=request.user)
        return render(request, 'perfil.html',{'emps':emps})
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')

        usuario = User.objects.filter(username=username).exclude(id=request.user.id)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome de usuário')
            return redirect('/perfil')
        
        request.user.username = username
        request.user.email = email
        request.user.first_name = primeiro_nome
        request.user.last_name = ultimo_nome
        request.user.save()
        messages.add_message(request, constants.SUCCESS, 'Dados alterado com sucesso')

        return redirect('/perfil')

@login_required(login_url='/auth/login')
def enviar_projeto(request):
    arquivo = request.FILES.get('file')
    id_emp = request.POST.get('id')

    emp = Emprego.objects.get(id=id_emp)

    emp.arquivo_final = arquivo
    emp.status = 'AA'
    emp.save()
    return redirect('/perfil')
