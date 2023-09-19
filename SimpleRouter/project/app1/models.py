from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    create_by=models.CharField(max_length=50)
    
    