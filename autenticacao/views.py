from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.messages import constants

def cadastro(request):
    # Como a requisição/request veio
    # Requisição pela url
    if request.method == "GET":
        # Se usuário está autenticado. Evita que acesse o cadastro e o login se já estiver.
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    # Requisição por formulário
    elif request.method == "POST":
        # return HttpResponse('Recebido POST')
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        # Se senhas forem diferentes
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/cadastro')

        # Se usuário não digitar um nome de usuário ou se não digitar snha. Só espaços não são contados (strip os tira).
        if len(usuario.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/cadastro')

        # Evita que usuários já cadastrados façam um novo cadastro
        user = User.objects.filter(username=usuario)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome')
            return redirect('/cadastro')

        try:
            # Tentará criar um novo usuário
            user = User.objects.create_user(username = usuario, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return redirect('/login')
        except Exception as erro:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro')


def login(request):

    if request.method == "GET":
        # Se usuário está autenticado. Evita que acesse o cadastro e o login se já estiver.
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        # Autenticação, ve se há um usuário no banco de dados com usuário e senha.
        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Nome de usuário ou senha inválidos')
            return redirect('/login')
        else:
            auth.login(request, usuario)
            return redirect('/')

def sair(request):
    auth.logout(request)
    return redirect('/login')
