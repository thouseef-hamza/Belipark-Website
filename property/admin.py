from django.contrib import admin

# Register your models here.
from property.models import Property,PropertyGallery

admin.site.register(Property)
admin.site.register(PropertyGallery)