from django.db import models

# Create your models here.


class Features(models.Model):
    title_name=models.CharField(max_length=300)
    description=models.TextField()
    
class Plans(models.Models):
    