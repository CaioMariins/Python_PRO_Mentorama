from django.db import models
from datetime import datetime as dt
# Create your models here.

class ProjetoDjango(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField("Publicado em",default=dt.now())
    
    def __str__(self):
        return self.titulo