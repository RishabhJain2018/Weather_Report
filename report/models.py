from django.db import models

# Create your models here.

class City(models.Model):
	city=models.CharField(max_length=200)
