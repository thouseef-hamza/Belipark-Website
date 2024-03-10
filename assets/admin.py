from django.contrib import admin
# Register your models here.
from assets.models import Property,Amenity,Service,Project,ImageGallery,ProjectPlotLayout
from django.contrib.auth.models import User,Group

admin.site.register(Property)
admin.site.register(Amenity)
admin.site.register(Service)
admin.site.register(ImageGallery)
admin.site.register(ProjectPlotLayout)
admin.site.register(Project)
admin.site.unregister(User)
admin.site.unregister(Group)
