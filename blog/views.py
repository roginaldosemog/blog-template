from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category
from .forms import ArticleForm, CategoryForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Article
    ordering = ['-created_at']
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Article
    template_name = 'article/article.html'

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/add_article.html'

class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/update_article.html'

class DeleteArticleView(DeleteView):
    model = Article
    success_url = reverse_lazy('home')
    template_name = 'article/delete_article.html'

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/add_category.html'