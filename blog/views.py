from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import ArticleForm

class HomeView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'