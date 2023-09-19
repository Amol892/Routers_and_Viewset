from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50)
    r_date=models.DateField()
    budget=models.FloatField()