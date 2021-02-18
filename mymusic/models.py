from django.db import models
from django.db.models import Model

# Create your models here.
class musiclist(models.Model):
    Title = models.CharField(max_length=50)
    Link = models.URLField(max_length=200)
    Desc = models.CharField(max_length=100)


def __str__(self): 
        return self.Title 
  
class Meta: 
    db_table = 'mymusic'