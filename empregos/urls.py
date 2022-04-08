from django.urls import path
from . import views

urlpatterns = [
    path('',views.encontrar_emps, name="encontrar_emps"),
    path('aceitar_emp/<int:id>/', views.aceitar_emp, name="aceitar_emp")
]