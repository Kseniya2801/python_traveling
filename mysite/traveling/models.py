from django.db import models
import datetime
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id',]






class Traveling(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    # slug = models.SlugField(max_length=255, unique=true, verbose_name= 'URL')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True) #запретим удалять категории, на которые есть ссылки из traveling; класс categoty дб выше по расположению этого классы

    def __str__(self): # выводит названия статей при выборке Traveling.objects.all()
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})

    class Meta:
        verbose_name='Популярные места отдыха'
        verbose_name_plural = 'Популярные места отдыха'
        ordering = ['time_create', 'title']




