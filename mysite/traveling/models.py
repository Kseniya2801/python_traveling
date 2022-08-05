from django.db import models

# Create your models here.

class Traveling(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    def __str__(self): # выводит названия статей при выборке Traveling.objects.all()
        return self.title

