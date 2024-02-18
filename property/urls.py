from django.urls import path
from property import views

urlpatterns = [
    path("",views.PropertyListView.as_view(),name="property_list"),
    path("detail/<int:id>/",views.PropertyRetriveView.as_view(),name="property_detail")
]
