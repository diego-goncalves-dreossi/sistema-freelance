from django.http import HttpResponse
from django.shortcuts import redirect, render

def cadastro(request):
    # Como a requisição/request veio
    # Requisição pela url
    if request.method == "GET":
        return render(request, 'cadastro.html')
    # Requisição por formulário
    elif request.method == "POST":
        # return HttpResponse('Recebido POST')
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        # Se senhas forem diferentes
        if not senha == confirmar_senha:
            return redirect('/cadastro')

        # Se usuário não digitar um nome de usuário ou se não digitar snha. Só espaços não são contados.
        if len(usuario.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/cadastro')

        #user = User.objects.filter(username=username)

        #if user.exists():
        #    return redirect('/auth/cadastro')

        return HttpResponse('Chegou no fim de POST')

def login(request):
    return render(request,'login.html')
