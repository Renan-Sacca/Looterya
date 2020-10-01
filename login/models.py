from django.db import models
from Home.models import fichas

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    senha = models.CharField(max_length=50)