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
