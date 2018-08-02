from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=10)
    steps = models.TextField(max_length = 200)
    picture = models.ImageField(upload_to='.' , blank=True)
    widget  = models.CharField(max_length=10)

    def get_absoulte_url(self):
        return "/recipe/{}/".format(self.id)
