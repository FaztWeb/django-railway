
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.render_articles, name='articles')
]