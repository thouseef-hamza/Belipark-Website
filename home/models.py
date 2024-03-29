from django.db import models
from django.utils import timezone
# Create your models here.


class ContactUS(models.Model):
    full_name = models.CharField(max_length=125)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image=models.ImageField(upload_to="blogs/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class HomeGallery(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="homegallery/")
    
    def __str__(self) -> str:
        return self.title

class AboutUS(models.Model):
    content=models.TextField()
    image=models.ImageField(upload_to="about/")
    
    def __str__(self):
        return self.content


class Director(models.Model):
    aboutus=models.ForeignKey(AboutUS,related_name="directors",on_delete=models.CASCADE)
    full_name=models.CharField(max_length=155)
    image=models.ImageField(upload_to="directors")
    position=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.full_name

class Carousel(models.Model):
    image=models.ImageField(upload_to="carousel/")
    created_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return "Carousel Image %s" % self.id

class Faculty(models.Model):
    image=models.ImageField(upload_to="faculty/")
    title_name=models.TextField(max_length=250)

    def __str__(self) -> str:
        return "Faculty Image of %s" % self.title_name
