from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .forms import AutorForm, Autor



# Create your views here.
def home(request):
    authors = Autor.objects.all()
    return render(request, 'libro/index.html', {'autores': authors})


def createauthor(request):
    if request.method == 'POST':
        author_form = AutorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('index')
    author_form = AutorForm()
    return render(request, 'libro/create_author.html', {'author_form': author_form})


def listauthor(request):
    authors = Autor.objects.all()
    return JsonResponse(serializers.serialize('json', authors), safe=False)
