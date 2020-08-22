from django.urls import path
from .views import HomeView, ArticleView, AddArticleView, UpdateArticleView, DeleteArticleView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('article/new/', AddArticleView.as_view(), name='add_article'),
    path('article/<int:pk>/edit/', UpdateArticleView.as_view(), name='update_article'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(), name='delete_article'),
    path('category/new/', AddCategoryView.as_view(), name='add_category'),
]
