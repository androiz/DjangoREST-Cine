from django.db import models

# Create your models here.
class Film(models.Model):
    url = models.CharField(max_length=255, unique=True)
    url_img = models.CharField(max_length=255)
    title = models.CharField(max_length=64)