from django.urls import path
from .views import*

urlpatterns = [
    path('', index),
    path('categories/', categories),
    path('categories/<int:catid>/',categories),

]