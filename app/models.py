import django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("home")