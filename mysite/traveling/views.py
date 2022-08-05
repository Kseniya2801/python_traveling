from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import*


# Create your views here.


# def index(request):
#     return HttpResponse('Путешествуй, Беларусь!')

# menu = ['Информация о сайте','Добавить статью','Обратная связь','Войти']
menu = [
    {'title': 'Информация о сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name':'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}

]

def index(request):
    posts = Traveling.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Путешествуй, Беларусь!'
    }
    return render(request, 'traveling/index.html', context=context)


def about(request):
    return render(request, 'traveling/about.html', {'menu':menu, 'title': 'Информация о сайте'})


def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id= {post_id}')


# def categories(request, catid):
#     return HttpResponse(f'<h1>Категории</h1><p>{catid}</p>')



# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1> Увы, страница не найдена :( </h1>')


