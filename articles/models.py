from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import CustomUser
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64)
    auther = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    abstract = models.TextField(max_length=256)
    text = models.TextField(blank=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles_detail", args=[self.id])
