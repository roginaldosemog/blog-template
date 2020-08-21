from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    ordering = ['-id']

class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'

class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'update_article.html'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
