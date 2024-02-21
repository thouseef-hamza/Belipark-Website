from django.urls import path
from assets import views

app_name="assets"

urlpatterns = [
    path("property/",views.propertiesList,name="property_list"),
    path("property/detail/<int:id>/",views.getDetailProperty,name="property_detail"),
    path("projects/",views.ProjectListView.as_view(),name="project_list"),
    path("projects/detail/<int:id>/",views.ProjectRetriveView.as_view(),name="project_detail"),
]
