from django.db import models
import os
# Create your models here.


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="amenity_images/")

    def __str__(self):
        return self.name


def property_gallery_upload_path(instance, filename):
    property_name = instance.property_name.title.replace(
        " ", "_"
    )
    return os.path.join("property", property_name, "images", filename)


class Property(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_bedrooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    description = models.TextField()
    year_built = models.IntegerField(
        null=True, blank=True
    )  
    amenities = models.ManyToManyField(
        Amenity
    ) 
    main_photo = models.ImageField(
        upload_to="property_photos/"
    )  
    created_at = models.DateTimeField(
        auto_now_add=True
    )  
    updated_at = models.DateTimeField(
        auto_now=True
    )  
class PropertyGallery(models.Model):
    property_name=models.ForeignKey(Property,on_delete=models.CASCADE,related_name="property_images")
    image = models.ImageField(upload_to=property_gallery_upload_path)
