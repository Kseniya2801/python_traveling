from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Путешествуй, Беларусь!')

def categories(request, catid):
    return HttpResponse(f'<h1>Категории</h1><p>{catid}</p>')

# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1> Увы, страница не найдена :( </h1>')


