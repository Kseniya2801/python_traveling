from django.contrib import admin
from .models import*

# Register your models here.

class TravelingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') #эти поля будут отображаться в админке
    list_display_links = ('id', 'title') #на этих полях будут формироваться ссылки
    search_fields = ('title', 'content') #поиск будет производиться только по этим полям
    list_editable = ("is_published",) #обязательно запятую, поле, которе можно редактировать в админке
    list_filter = ('is_published', 'time_create') #поля.по которым можно фильтровать


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) #здесь обязательно нужно ставить запятую в скобках, если элемент один, т.к. мы здесь должны передавать кортеж! а не строку !


admin.site.register(Traveling, TravelingAdmin)
admin.site.register(Category, CategoryAdmin)

