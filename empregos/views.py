from django.http import HttpResponse
from django.shortcuts import render
from .models import Emprego

def encontrar_emps(request):
    if request.method == 'GET':
        emps = Emprego.objects.filter(reservado = False)
        print(emps)
        return render(request, 'encontrar_emps.html',{'emps':emps})
    if request.method == 'POST':
        preco_minimo = request.POST.get('preco_minimo')