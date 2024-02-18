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
    class PropertyAvailability(models.TextChoices):
        SOLD_OUT="sold_out","SOLD OUT"
        FOR_RENT="for_rent","For Rent"
        FOR_SALE="for_sale","For Sale"
        AVAILABLE="available","Available"
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_bedrooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    description = models.TextField()
    availability=models.CharField(max_length=20,choices=PropertyAvailability.choices,default=PropertyAvailability.AVAILABLE)
    year_built = models.IntegerField(
        null=True, blank=True
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

class Projects(models.Model):
    name = models.CharField(max_length=255)
    