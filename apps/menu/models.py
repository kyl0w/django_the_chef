from django.db import models

# Create your models here.
class Category(models.Model):
    pass

class Menu(models.Model):
    
    name = models.CharField(max_length=255)
    