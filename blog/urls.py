from django.urls import path
from .views import HomeView, ArticleView, AddArticleView, UpdateArticleView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('article/new/', AddArticleView.as_view(), name="add_article"),
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name="update_article"),
]
