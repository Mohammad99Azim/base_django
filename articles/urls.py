from django.urls import path

from .views import ArticlesListView, ArticlesDetailView, ArticlesCreateView, ArticlesUpdateView, ArticlesDeleteView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles_list'),
    path('<int:pk>/', ArticlesDetailView.as_view(), name='articles_detail'),
    path('articles/create/', ArticlesCreateView.as_view(), name='create_articles'),
    path('update/<int:pk>/', ArticlesUpdateView.as_view(), name='update_article'),
    path('delete/<int:pk>/', ArticlesDeleteView.as_view(), name='delete_article')
]
