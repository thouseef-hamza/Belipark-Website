from django.contrib import admin
from .models import ContactUS, Blog, HomeGallery, AboutUS, Director, Carousel,Faculty
from django.utils.html import format_html

# Inline model admins

admin.site.register(Faculty)
class DirectorInline(admin.TabularInline):
    model = Director

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(
                    obj.image.url
                )
            )
        return "-"

    image_preview.short_description = "Image Preview"
    readonly_fields = ("image_preview",)
    
# Register your models here.
@admin.register(ContactUS)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number")
    search_fields = ("full_name", "email", "phone_number")
    list_per_page = 20


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview", "created_at")
    search_fields = ("title", "content")
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                    obj.image.url
                )
            )
        return "-"

    image_preview.short_description = "Image"
    readonly_fields = ("image_preview",)


@admin.register(HomeGallery)
class HomeGalleryAdmin(admin.ModelAdmin):
    list_display = ("title","image_preview")
    search_fields = ("title",)
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />'.format(obj.image.url))
        return "-"

    image_preview.short_description = "Image Preview"
    readonly_fields = ("image_preview",)


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("id","image_preview")
    search_fields = ("id",)
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />'.format(obj.image.url))
        return "-"

    image_preview.short_description = "Image Preview"
    readonly_fields = ("image_preview",)


@admin.register(AboutUS)
class AboutUSAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    search_fields = ("id",)
    list_per_page = 20
    inlines = [DirectorInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                    obj.image.url
                )
            )
        return "-"

    image_preview.short_description = "Image Preview"
    readonly_fields = ("image_preview",)
