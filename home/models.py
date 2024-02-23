from django.db import models

# Create your models here.


class ContactUS(models.Model):
    full_name=models.CharField(max_length=125)
    email=models.EmailField()
    subject=models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField()
    
    def __str__(self) -> str:
        return self.full_name