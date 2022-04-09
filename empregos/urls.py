from django.urls import path
from . import views

urlpatterns = [
    path('',views.encontrar_emps, name="encontrar_emps"),
    path('aceitar_emp/<int:id>/', views.aceitar_emp, name="aceitar_emp"),
    path('perfil/', views.perfil, name="perfil"),
    path('enviar_projeto/', views.enviar_projeto, name="enviar_projeto"),
    path('suas_vagas/',views.suas_vagas, name='suas_vagas'),
    path('criar_vagas/',views.criar_vagas, name='criar_vagas')
]