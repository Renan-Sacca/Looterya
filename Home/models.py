from django.db import models
from datetime import datetime

class fichas(models.Model):
    link = models.TextField()
    valor = models.IntegerField()
    nome_ficha = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    



"""class Receita(models.Model):
   nome_receita = models.CharField(max_lenght=200)
   ingredientes = models.TextField()
 modo_preparo = models.textField()
  tempo_preparo = models.IntegerField()
   rendimento = models.CharField(max_lenght=100)
   categoria = models.CharField(max_lenght=100)
   date_receita = models.DateTimeField(default=datetime.now, blank=true)"""
