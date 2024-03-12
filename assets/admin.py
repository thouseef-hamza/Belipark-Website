from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Amenity,
    Service,
    Property,
    Project,
    ImageGallery,
    ProjectPlotLayout,
    Infratech,
    InfraTechImages,
)
from django.contrib.auth.models import Group,User
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Service)
@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />'.format(obj.image.url))
        return "-"

    image_preview.short_description = "Image Preview"
    readonly_fields = ("image_preview",)


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    extra = 1
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />'.format(obj.image.url))
        return '-'

    image_preview.short_description = 'Image Preview'
    readonly_fields = ('image_preview',)

class AmenityInline(admin.TabularInline):
    model = Project.amenity.through
    verbose_name="Amenity"
    verbose_name_plural="Amenities"
    extra = 1
    
    def amenity_image_preview(self, obj):
        if obj.amenity.image:
            return format_html('<img src="{}" height="50" />'.format(obj.amenity.image.url))
        return '-'

    amenity_image_preview.short_description = 'Amenity Image Preview'
    readonly_fields = ('amenity_image_preview',)

class ProjectPlotLayoutInline(admin.TabularInline):
    model = ProjectPlotLayout
    extra = 1 

    def image_preview(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.image.url))

    image_preview.short_description = "Image Preview"
    readonly_fields = ("image_preview",)

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "property_name",
        "address",
        "price",
        "availability",
        "image_preview",
    )
    search_fields = ("property_name", "address")
    list_per_page = 20
    inlines=[ImageGalleryInline]

    def image_preview(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.main_photo.url))

    image_preview.short_description = "Image Preview"
    readonly_fields=("image_preview",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "address", "display_main_photo")
    search_fields = ("project_name", "address")
    exclude=("amenity",)
    list_per_page = 20
    inlines=[ImageGalleryInline,AmenityInline,ProjectPlotLayoutInline]

    def display_main_photo(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.main_photo.url))

    display_main_photo.short_description = "Main Photo"

# @admin.register(ProjectPlotLayout)
# class ProjectPlotLayoutAdmin(admin.ModelAdmin):
#     list_display = ("project", "display_image")
#     search_fields = ("project__project_name",)
#     list_per_page = 20

#     def display_image(self, obj):
#         return format_html('<img src="{}" height="50" />'.format(obj.image.url))

#     display_image.short_description = "Image"


@admin.register(Infratech)
class InfratechAdmin(admin.ModelAdmin):
    list_display = ("content",)
    list_per_page = 20


@admin.register(InfraTechImages)
class InfraTechImagesAdmin(admin.ModelAdmin):
    list_display = ("display_image",)
    list_per_page = 20

    def display_image(self, obj):
        return format_html('<img src="{}" height="50" />'.format(obj.image.url))

    display_image.short_description = "Image"
