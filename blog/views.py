from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class HomeView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'