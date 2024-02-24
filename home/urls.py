from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path("",views.homeView,name="home_view"),
    path("about/",views.aboutView,name="about_view"),
    path("contact/us/",views.createContact,name="contact_us"),
    path("blogs/",views.blogList,name="blog_list"),
    path("blog/detail/<int:id>/",views.blogDetail,name="blog_detail"),
]
