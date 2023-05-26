from django.db import models

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=150)
    status = models.CharField(max_length=100)
    foto = models.ImageField()