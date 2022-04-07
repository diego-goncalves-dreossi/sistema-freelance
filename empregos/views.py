from django.http import HttpResponse
from django.shortcuts import render
from .models import Emprego

def encontrar_emps(request):
    if request.method == 'GET':
        emps = Emprego.objects.filter(reservado = False)
        #print(emps)
        
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')
        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_minimo')
        categoria = request.GET.get('categoria')

        # Se um dos filtros foi usado
        if preco_minimo or preco_maximo or prazo_minimo or prazo_maximo or categoria:
            pass


        return render(request, 'encontrar_emps.html',{'emps':emps})
        return HttpResponse(preco_minimo)