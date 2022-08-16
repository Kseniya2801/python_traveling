from .models import *
from django.core.cache import cache



# menu = ['Информация о сайте','Добавить статью','Обратная связь','Войти']
menu = [
    {'title': 'Информация о сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name':'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},

]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats =Category.objects.all()
            cache.set('cats', cats, 60)


        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context