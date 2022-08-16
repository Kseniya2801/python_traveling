from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import*

# Register your models here.

class TravelingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published') #эти поля будут отображаться в админке
    list_display_links = ('id', 'title') #на этих полях будут формироваться ссылки
    search_fields = ('title', 'content') #поиск будет производиться только по этим полям
    list_editable = ("is_published",) #обязательно запятую, поле, которoе можно редактировать в админке
    list_filter = ('is_published', 'time_create') #поля.по которым можно фильтровать
    prepopulated_fields = {'slug': ('title',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) #здесь обязательно нужно ставить запятую в скобках, если элемент один, т.к. мы здесь должны передавать кортеж! а не строку !
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Traveling, TravelingAdmin)
admin.site.register(Category, CategoryAdmin)

