from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView,DeleteView

from .models import Article


# Create your views here.

class ArticlesListView(ListView):
    template_name = "articles_list.html"
    model = Article
    context_object_name = "articles_list"


class ArticlesDetailView(DetailView):
    template_name = "articles_detail.html"
    model = Article
    context_object_name = "article_detail"


class ArticlesCreateView(CreateView):
    template_name = "articles_create.html"
    fields = ["title", "auther", "abstract", "text"]
    model = Article


class ArticlesUpdateView(UpdateView):
    template_name = "articles_update.html"
    fields = ["title", "auther", "abstract", "text"]
    model = Article


class ArticlesDeleteView(DeleteView):
    template_name = "articles_delete.html"
    model = Article
    success_url = reverse_lazy("articles_list")
