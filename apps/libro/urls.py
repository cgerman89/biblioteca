from django.urls import path
from .views import home, createauthor, listauthor
urlpatterns = [
    path('', home, name='index'),
    path('crear_autor/', createauthor, name='crear_autor'),
    path('listar_autores/', listauthor, name='listar_autor'),
]