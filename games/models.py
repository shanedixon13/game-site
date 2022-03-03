from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Game(models.Model):
    title=models.CharField(max_length=200)
    link=models.URLField()
    body=models.TextField()
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_on=models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default="None")
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game_detail', args=[str(self.id)])