from django.db import models

# Create your models here.


class ContactUS(models.Model):
    full_name = models.CharField(max_length=125)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
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
    
    def __str__(self):
        return self.content
    

class Director(models.Model):
    aboutus=models.ForeignKey(AboutUS,related_name="directors_images",on_delete=models.CASCADE)
    full_name=models.CharField(max_length=155)
    image=models.ImageField(upload_to="directors")
    position=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.full_name
    
class Carousel(models.Model):
    image=models.ImageField(upload_to="carousel/")
    