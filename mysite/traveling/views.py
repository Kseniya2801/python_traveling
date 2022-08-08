from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import*
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





class TravelingHome(ListView):
    model = Traveling
    template_name = 'traveling/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Путешествуй, Буларусь!'
        context['cat_selected'] = 0
        context['menu'] = menu

        return context

    def get_queryset(self):
        return Traveling.objects.filter(is_published= True) #выведет на экран лишь те статьи, которые отмечены опубликованными


# def index(request):
#     posts = Traveling.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Путешествуй, Беларусь!',
#         'cat_selected':0,
#     }
#     return render(request, 'traveling/index.html', context=context)


def about(request):
    return render(request, 'traveling/about.html', {'menu':menu, 'title': 'Информация о сайте'})



class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'traveling/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'traveling/addpage.html', {'form':form,'menu':menu, 'title':'Добавление статьи'})



def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception):
    return HttpResponseNotFound('')


class ShowPost(DetailView):
    model = Traveling
    template_name = 'traveling/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Traveling, slug=post_slug)
#     cats = Category.objects.all()
#
#     context = {
#         'post': post,
#         'cats': cats,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'traveling/post.html', context=context)




class TravelingCategory(ListView):
    model = Traveling
    template_name = 'traveling/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Traveling.object.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория -' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = Traveling.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#
#     if len(posts)== 0:
#         raise Http404('Увы, страница не найдена:(')
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Отображение по категориям...',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'traveling/index.html', context=context)






