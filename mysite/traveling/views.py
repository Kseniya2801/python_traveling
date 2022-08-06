from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
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
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Путешествуй, Беларусь!',
        'cat_selected':0,
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

def pageNotFound(request, exception):
    return HttpResponseNotFound('')

def show_post(request, post_id):
    post = get_object_or_404(Traveling, pk=post_id)
    cats = Category.objects.all()

    context = {
        'post': post,
        'cats': cats,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'traveling/post.html', context=context)


def show_category(request, cat_id):
    posts = Traveling.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts)== 0:
        raise Http404('Увы, страница не найдена:(')

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям...',
        'cat_selected': cat_id,
    }
    return render(request, 'traveling/index.html', context=context)






