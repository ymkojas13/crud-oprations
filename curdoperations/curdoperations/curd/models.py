from django.db import models

# Create your models here.

class Curdoperations(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
