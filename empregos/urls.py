from django.urls import path
from . import views

urlpatterns = [
    path('encontrar/',views.encontrar_emps, name="encontrar_emps")
]