from django.contrib import admin
from .models import Blog,ContactUS,HomeGallery,Carousel,AboutUS,Director
from assets.models import Infratech,InfraTechImages
# Register your models here.

admin.site.register(Blog)
admin.site.register(ContactUS)
admin.site.register(HomeGallery)
admin.site.register(Carousel)
admin.site.register(AboutUS)
admin.site.register(Director)
admin.site.register(Infratech)
admin.site.register(InfraTechImages)

