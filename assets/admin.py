from django.contrib import admin

# Register your models here.
from assets.models import Property,Amenity,Gallery,Service,Project

admin.site.register(Property)
admin.site.register(Amenity)
admin.site.register(Gallery)
admin.site.register(Service)
admin.site.register(Project)
