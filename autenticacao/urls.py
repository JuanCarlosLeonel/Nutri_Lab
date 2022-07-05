from django.urls import path, include
from . views import cadastro, logar

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('logar/', logar, name='logar'),
]
