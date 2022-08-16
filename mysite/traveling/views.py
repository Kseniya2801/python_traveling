from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



from .forms import*
from .models import*
from .utils import *


# Create your views here.


# def index(request):
#     return HttpResponse('Путешествуй, Беларусь!')




class TravelingHome(DataMixin, ListView):
    model = Traveling
    template_name = 'traveling/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Путешествуй, Беларусь!')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Traveling.objects.filter(is_published=True).select_related('cat') #выведет на экран лишь те статьи, которые отмечены опубликованными


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



class AddPage(LoginRequiredMixin, DataMixin, CreateView): #только для авторизованных пользователей
    form_class = AddPostForm
    template_name = 'traveling/addpage.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items())+list(c_def.items()))

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


@login_required #только для зарегистрированных пользователей
def contact(request):
    return HttpResponse('Обратная связь')



def pageNotFound(request, exception):
    return HttpResponseNotFound('')





class ShowPost(DataMixin, DetailView):
    model = Traveling
    template_name = 'traveling/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
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




class TravelingCategory(DataMixin, ListView):
    model = Traveling
    template_name = 'traveling/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Traveling.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория -' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterCreationForm
    template_name = 'traveling/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form): #метод вызывается при успешной регистрации
        user = form.save() #добавляем пользователя  в бд
        login(self.request, user) #функция авторизовывает сразу пользователя
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'traveling/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self): #метод будет срабатывать если введённый пользователь существует (т.е. форма прошла валидацию)
    #     return reverse_lazy('home')

# def login(request):
#     return HttpResponse('Авторизация')


def logout_user(request):
    logout(request)
    return redirect('login')
