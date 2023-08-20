from django.urls import path
from . import views

urlpatterns = [
    path('get_articles/', views.get_articles, name='get_articles'),
]