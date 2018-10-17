from django.db import models
from django.urls import reverse

# Create your models here.
class Diary(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=10)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("diary:detail-view" , kwargs={'id':self.id})
