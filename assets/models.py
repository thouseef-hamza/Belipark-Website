from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="amenity_images/")

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Property(models.Model):
    class PropertyAvailability(models.TextChoices):
        SOLD_OUT="sold_out","SOLD OUT"
        FOR_RENT="for_rent","For Rent"
        FOR_SALE="for_sale","For Sale"
        AVAILABLE="available","Available"
        
    property_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_bedrooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    description = models.TextField()
    availability=models.CharField(max_length=20,choices=PropertyAvailability.choices,default=PropertyAvailability.AVAILABLE)
    main_photo = models.ImageField(
        upload_to="property_photos/"
    )  
    created_at = models.DateTimeField(
        auto_now_add=True
    )  
    updated_at = models.DateTimeField(
        auto_now=True
    )  
    
    def __str__(self) -> str:
        return self.property_name

class Project(models.Model):
    project_name = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    description=models.TextField()
    amenity=models.ManyToManyField(Amenity)
    service = models.ManyToManyField(Service)
    main_photo = models.ImageField(upload_to="project_photos/")

    def __str__(self) -> str:
        return self.project_name


class ImageGallery(models.Model):
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE,related_name="property_images",null=True,blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="project_images",null=True,blank=True)
    image = models.ImageField(upload_to="assets/images/")
    
    def __str__(self) -> str:
        return self.property_id.property_name if self.property_id.property_name else self.project if self.project.project_name else "None"

class ProjectPlotLayout(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="project_plotlayout")
    image=models.ImageField(upload_to="plot/")
    
    def __str__(self) -> str:
        return self.project.project_name

class Infratech(models.Model):
    content=models.TextField()
    
    def __str__(self) -> str:
        return "Infratech Description"
    
class InfraTechImages(models.Model):
    image=models.ImageField(upload_to="infratech/",null=True,blank=True)
    
    def __str__(self) -> str:
        return "Infratech Images"
    